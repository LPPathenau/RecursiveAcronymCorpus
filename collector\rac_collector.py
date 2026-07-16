# -*- coding: utf-8 -*-
"""
RecursiveAcronymCorpus 采集器
============================

自动采集计算机科学领域的递归缩略语

数据来源:
- Wikipedia "Recursive acronym" 词条
- Jargon File
- GitHub API
- 项目官方文档

作者: Li Pengpeng
机构: 河南农业大学语言智能研究中心
版本: v1.0
"""

import os
import re
import json
import time
import csv
import requests
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from pathlib import Path
import argparse

# ==================== 配置 ====================

@dataclass
class CollectorConfig:
    """采集器配置"""
    output_dir: str = "./data"
    data_file: str = "./data/rac_v1.csv"
    delay_seconds: float = 1.0
    timeout: int = 30
    max_results: int = 500

# ==================== 数据模型 ====================

@dataclass
class RecursiveAcronym:
    """递归缩略语条目"""
    acronym: str = ""
    full_form: str = ""
    category: str = ""
    sub_category: str = ""
    year: str = ""
    origin: str = ""
    domain: str = ""
    confidence: str = "Medium"
    motivation: str = ""
    recursive_marker: str = ""
    notes: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "acronym": self.acronym,
            "full_form": self.full_form,
            "category": self.category,
            "sub_category": self.sub_category,
            "year": self.year,
            "origin": self.origin,
            "domain": self.domain,
            "confidence": self.confidence,
            "motivation": self.motivation,
            "recursive_marker": self.recursive_marker,
            "notes": self.notes
        }

# ==================== Wikipedia采集器 ====================

class WikipediaCollector:
    """Wikipedia递归缩写采集器"""
    
    WIKI_API = "https://en.wikipedia.org/w/api.php"
    
    def __init__(self, config: CollectorConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RecursiveAcronymCorpus-Collector/1.0'
        })
    
    def collect(self) -> List[RecursiveAcronym]:
        """采集Wikipedia递归缩写"""
        acronyms = []
        
        # 1. 获取主词条内容
        main_content = self._fetch_page("Recursive_acronym")
        if main_content:
            entries = self._parse_wiki_list(main_content)
            acronyms.extend(entries)
        
        # 2. 获取相关词条
        related_pages = self._get_related_pages("Recursive_acronym")
        for page in related_pages[:20]:  # 限制数量
            content = self._fetch_page(page)
            if content:
                entries = self._parse_wiki_list(content)
                acronyms.extend(entries)
            time.sleep(self.config.delay_seconds)
        
        return acronyms
    
    def _fetch_page(self, title: str) -> Optional[str]:
        """获取页面内容"""
        params = {
            "action": "query",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
            "format": "json"
        }
        
        try:
            response = self.session.get(
                self.WIKI_API, 
                params=params, 
                timeout=self.config.timeout
            )
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            for page_id, page_data in pages.items():
                return page_data.get("extract", "")
        except Exception as e:
            print(f"获取页面失败 {title}: {e}")
        return None
    
    def _get_related_pages(self, title: str) -> List[str]:
        """获取相关页面"""
        params = {
            "action": "query",
            "titles": title,
            "prop": "links",
            "pllimit": 50,
            "format": "json"
        }
        
        try:
            response = self.session.get(
                self.WIKI_API, 
                params=params, 
                timeout=self.config.timeout
            )
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            for page_id, page_data in pages.items():
                links = page_data.get("links", [])
                return [link["title"] for link in links]
        except Exception as e:
            print(f"获取链接失败: {e}")
        return []
    
    def _parse_wiki_list(self, content: str) -> List[RecursiveAcronym]:
        """解析Wikipedia内容"""
        entries = []
        
        # 常见递归标记模式
        markers = [
            r"(?:is|Is|IS|ain't|Ain't|ARE|are)\s+(?:a|an|not|Not|NOT)",
            r"(?:stands for|standsfor)",
            r"(?:was|Was|WAS)\s+(?:originally|initially|created)",
            r"(?:Yet Another|yet another|YAA)"
        ]
        
        # 分割内容行
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # 跳过太短的行
            if len(line) < 10:
                continue
            
            # 检测可能的递归缩写
            for marker in markers:
                if re.search(marker, line, re.IGNORECASE):
                    entry = self._extract_entry(line, i, lines)
                    if entry and entry.acronym:
                        entries.append(entry)
                    break
        
        return entries
    
    def _extract_entry(self, line: str, idx: int, lines: List[str]) -> Optional[RecursiveAcronym]:
        """从行中提取条目"""
        entry = RecursiveAcronym()
        
        # 尝试提取缩略语（全大写词）
        acronym_match = re.search(r'\b([A-Z]{2,6})\b', line)
        if acronym_match:
            entry.acronym = acronym_match.group(1)
        
        # 提取展开式
        # 模式: ACRONYM ... meaning
        patterns = [
            r'(?:^|\s)([A-Z]{2,6})[,.\s]+(?:which stands for|stands for|is|means|'
            r'Ain\'t|Isn\'t|Not|A\s+recursive\s+acronym\s+for)[,.\s]+([^\n.]+)',
            r'(?:^|\s)([A-Z]{2,6})[,.\s]+(?:GNU|YAML|WINE|YAF|PHP|PINE|LAME|PNG)[,.\s]+([^\n.]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                entry.full_form = match.group(0)
                break
        
        if not entry.full_form:
            entry.full_form = line[:200].strip()
        
        # 分类
        entry.category = self._classify_category(line)
        
        # 领域
        entry.domain = self._classify_domain(line)
        
        # 年份
        year_match = re.search(r'\b(19[5-9]\d|20[0-2]\d)\b', line)
        if year_match:
            entry.year = year_match.group(1)
        
        # 置信度
        entry.confidence = "Medium"
        
        return entry
    
    def _classify_category(self, text: str) -> str:
        """分类"""
        text_lower = text.lower()
        
        if "not" in text_lower or "ain't" in text_lower:
            return "Full_Recursive"
        elif "is" in text_lower and len(text) < 100:
            return "Self_Referential"
        elif "was" in text_lower:
            return "Partial_Recursive"
        else:
            return "Self_Referential"
    
    def _classify_domain(self, text: str) -> str:
        """领域分类"""
        text_lower = text.lower()
        
        domains = {
            "OS": ["operating system", "kernel", "linux", "unix"],
            "Language": ["programming language", "python", "ruby", "php", "java"],
            "Format": ["markup", "format", "serialization", "yaml", "json", "xml"],
            "Tool": ["editor", "compiler", "linter", "tool"],
            "Web": ["web", "browser", "html", "css", "javascript"],
            "Database": ["database", "sql", "mongodb", "nosql"],
            "BigData": ["hadoop", "spark", "kafka", "big data", "mapreduce"],
            "Container": ["docker", "kubernetes", "container", "k8s"]
        }
        
        for domain, keywords in domains.items():
            for kw in keywords:
                if kw in text_lower:
                    return domain
        
        return "General"

# ==================== GitHub采集器 ====================

class GitHubCollector:
    """GitHub项目名采集器"""
    
    def __init__(self, config: CollectorConfig, token: str = None):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RecursiveAcronymCorpus-Collector',
            'Accept': 'application/vnd.github.v3+json'
        })
        if token:
            self.session.headers['Authorization'] = f'token {token}'
    
    def collect(self) -> List[RecursiveAcronym]:
        """采集GitHub项目"""
        acronyms = []
        
        # 搜索递归缩写项目
        search_terms = [
            "recursive acronym",
            "GNU's Not Unix",
            "YAML Ain't",
            "Wine Is Not",
            "Yet Another"
        ]
        
        for term in search_terms:
            results = self._search_repos(term)
            for result in results[:10]:
                entry = self._parse_repo(result)
                if entry:
                    acronyms.append(entry)
            time.sleep(self.config.delay_seconds)
        
        return acronyms
    
    def _search_repos(self, query: str) -> List[Dict]:
        """搜索仓库"""
        url = "https://api.github.com/search/repositories"
        params = {
            "q": f"{query} in:name,description",
            "per_page": 10,
            "sort": "stars"
        }
        
        try:
            response = self.session.get(url, params=params, timeout=self.config.timeout)
            if response.status_code == 200:
                return response.json().get("items", [])
        except Exception as e:
            print(f"搜索失败: {e}")
        return []
    
    def _parse_repo(self, repo: Dict) -> Optional[RecursiveAcronym]:
        """解析仓库信息"""
        entry = RecursiveAcronym()
        
        name = repo.get("name", "")
        if not name:
            return None
        
        entry.acronym = name.upper()[:6]
        entry.full_form = repo.get("description", "") or name
        entry.origin = repo.get("owner", {}).get("login", "")
        entry.year = repo.get("created_at", "")[:4] if repo.get("created_at") else ""
        entry.domain = self._classify_domain(entry.full_form)
        entry.confidence = "Low"
        entry.motivation = "Community"
        
        return entry
    
    def _classify_domain(self, text: str) -> str:
        """领域分类"""
        text_lower = text.lower()
        
        if "editor" in text_lower or "vim" in text_lower:
            return "Editor"
        elif "language" in text_lower or "parser" in text_lower:
            return "Language"
        elif "web" in text_lower or "framework" in text_lower:
            return "Web"
        elif "database" in text_lower or "sql" in text_lower:
            return "Database"
        elif "container" in text_lower or "docker" in text_lower:
            return "Container"
        
        return "General"

# ==================== 主采集器 ====================

class RACCollector:
    """RecursiveAcronymCorpus 主采集器"""
    
    def __init__(self, config: CollectorConfig = None):
        self.config = config or CollectorConfig()
        self.entries: List[RecursiveAcronym] = []
        os.makedirs(self.config.output_dir, exist_ok=True)
    
    def collect_all(self, github_token: str = None) -> List[RecursiveAcronym]:
        """采集所有来源"""
        all_entries = []
        
        # 1. Wikipedia采集
        print("📚 采集Wikipedia...")
        wiki_collector = WikipediaCollector(self.config)
        wiki_entries = wiki_collector.collect()
        print(f"  ✓ Wikipedia: {len(wiki_entries)} 条")
        all_entries.extend(wiki_entries)
        
        # 2. GitHub采集（可选）
        if github_token:
            print("🔍 采集GitHub...")
            github_collector = GitHubCollector(self.config, github_token)
            github_entries = github_collector.collect()
            print(f"  ✓ GitHub: {len(github_entries)} 条")
            all_entries.extend(github_entries)
        
        # 3. 去重合并
        self.entries = self._deduplicate(all_entries)
        print(f"\n总计: {len(self.entries)} 条（去重后）")
        
        return self.entries
    
    def _deduplicate(self, entries: List[RecursiveAcronym]) -> List[RecursiveAcronym]:
        """去重"""
        seen = set()
        unique = []
        
        for entry in entries:
            key = entry.acronym.upper()
            if key and key not in seen:
                seen.add(key)
                unique.append(entry)
        
        return unique
    
    def export_csv(self, filename: str = None) -> str:
        """导出CSV"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"rac_{timestamp}.csv"
        
        filepath = os.path.join(self.config.output_dir, filename)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'ID', 'Acronym', 'Full_Form', 'Category', 'Sub_Category',
                'Year', 'Origin', 'Domain', 'Confidence', 'Motivation',
                'Recursive_Marker', 'Notes'
            ])
            
            for i, entry in enumerate(self.entries, 1):
                writer.writerow([
                    f'RAC-{i:04d}',
                    entry.acronym,
                    entry.full_form,
                    entry.category,
                    entry.sub_category,
                    entry.year,
                    entry.origin,
                    entry.domain,
                    entry.confidence,
                    entry.motivation,
                    entry.recursive_marker,
                    entry.notes
                ])
        
        print(f"✓ 已导出: {filepath}")
        return filepath
    
    def export_json(self, filename: str = None) -> str:
        """导出JSON"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"rac_{timestamp}.json"
        
        filepath = os.path.join(self.config.output_dir, filename)
        
        data = [entry.to_dict() for entry in self.entries]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 已导出: {filepath}")
        return filepath

# ==================== 主程序 ====================

def main():
    parser = argparse.ArgumentParser(description='RecursiveAcronymCorpus 采集器')
    parser.add_argument('--output', '-o', default='./data', help='输出目录')
    parser.add_argument('--github-token', '-t', help='GitHub Token (可选)')
    parser.add_argument('--format', '-f', choices=['csv', 'json', 'both'], default='both', help='导出格式')
    parser.add_argument('--max', '-m', type=int, default=500, help='最大采集数量')
    
    args = parser.parse_args()
    
    # 配置
    config = CollectorConfig(
        output_dir=args.output,
        max_results=args.max
    )
    
    # 采集
    print("=" * 60)
    print("RecursiveAcronymCorpus 采集器")
    print("=" * 60)
    
    collector = RACCollector(config)
    collector.collect_all(github_token=args.github_token)
    
    # 导出
    if args.format in ['csv', 'both']:
        collector.export_csv()
    if args.format in ['json', 'both']:
        collector.export_json()
    
    print("=" * 60)
    print("采集完成!")

if __name__ == "__main__":
    main()
