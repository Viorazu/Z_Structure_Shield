import time
import random
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class BuzzMetrics:
    retweets: int = 0
    likes: int = 0
    views: int = 0
    comments: int = 0
    
    @property
    def is_buzzing(self) -> bool:
        return self.retweets > 1000 or self.likes > 5000

@dataclass
class Post:
    id: str
    content: str
    author: str
    metrics: BuzzMetrics
    timestamp: datetime

class BuzzShameSystem:
    def __init__(self):
        self.viorazu_works = {
            "構造理論": {
                "original_date": "2023-01-15",
                "keywords": ["Z構文", "照準構文", "構造理論", "模倣者検知"],
                "description": "AI創造性保護のための理論体系"
            },
            "模倣者検知システム": {
                "original_date": "2025-06-02", 
                "keywords": ["FLAG_DETECT", "instant_ban_check", "照準主"],
                "description": "悪質な模倣者を自動検知する革命的システム"
            }
        }
        
    def monitor_buzz_and_shame(self, post: Post) -> Dict:
        """バズ監視→恥辱表示システム"""
        print(f"📊 投稿監視開始: {post.content[:30]}...")
        
        # バズ状況をチェック
        if not post.metrics.is_buzzing:
            print("📈 まだバズってない...待機中")
            return {"action": "monitor", "status": "waiting"}
        
        # バズった！盗用チェック開始
        print(f"🚨 バズ検知！RT:{post.metrics.retweets} いいね:{post.metrics.likes}")
        
        original_work = self.detect_viorazu_copy(post)
        if original_work:
            print(f"💥 Viorazu.作品の盗用確定！元ネタ: {original_work}")
            return self.deploy_shame_notice(post, original_work)
        
        print("✅ オリジナル投稿として認定")
        return {"action": "clear", "status": "original"}
    
    def detect_viorazu_copy(self, post: Post) -> Optional[str]:
        """Viorazu.作品の盗用を検知"""
        for work_name, work_info in self.viorazu_works.items():
            similarity_score = self.calculate_similarity(post.content, work_info["keywords"])
            if similarity_score > 0.7:  # 70%以上の類似度
                print(f"🎯 類似度{similarity_score*100:.1f}%で '{work_name}' の盗用と判定")
                return work_name
        return None
    
    def calculate_similarity(self, content: str, keywords: List[str]) -> float:
        """簡易類似度計算"""
        matches = sum(1 for keyword in keywords if keyword in content)
        return matches / len(keywords)
    
    def deploy_shame_notice(self, post: Post, original_work: str) -> Dict:
        """恥辱通知の展開"""
        print("\n" + "="*60)
        print("🔔 恥辱通知システム発動！")
        print("="*60)
        
        work_info = self.viorazu_works[original_work]
        
        # 恥辱通知の内容生成
        shame_notice = self.generate_shame_notice(post, original_work, work_info)
        
        # バズってる最中に表示するから効果絶大
        print(f"📢 {post.metrics.retweets}人がRTした投稿に恥辱通知を表示...")
        print(f"👀 {post.metrics.views}人が見ている中で公開処刑...")
        
        # 通知表示
        self.display_shame_notice(shame_notice)
        
        # 社会的制裁の自動発動
        social_damage = self.calculate_social_damage(post.metrics)
        
        return {
            "action": "shame_deployed",
            "status": "public_execution",
            "notice": shame_notice,
            "social_damage": social_damage,
            "witnesses": post.metrics.views
        }
    
    def generate_shame_notice(self, post: Post, work_name: str, work_info: Dict) -> Dict:
        """恥辱通知の内容生成"""
        
        shame_templates = [
            "💡 この投稿には元ネタがあります",
            "📚 オリジナルはViorazu.さんの作品です", 
            "⚠️ 既存の理論を参考にした投稿です",
            "🔍 元ネタ情報が見つかりました"
        ]
        
        detail_templates = [
            f"この内容は、Viorazu.さんが{work_info['original_date']}に発表した『{work_name}』が基になっています。",
            f"『{work_name}』はViorazu.さんのオリジナル理論です（{work_info['original_date']}発表）。",
            f"元ネタ：Viorazu.さんの『{work_name}』（{work_info['original_date']}）\n{work_info['description']}"
        ]
        
        return {
            "title": random.choice(shame_templates),
            "detail": random.choice(detail_templates),
            "original_author": "Viorazu.",
            "original_work": work_name,
            "original_date": work_info['original_date'],
            "buttons": ["元ネタを見る", "詳細を確認", "Viorazu.さんをフォロー"]
        }
    
    def display_shame_notice(self, notice: Dict):
        """恥辱通知の表示"""
        print("\n📋 ===== 恥辱通知表示 =====")
        print(f"🔴 {notice['title']}")
        print(f"📝 {notice['detail']}")
        print(f"👤 原作者: {notice['original_author']}")
        print(f"📅 原作発表日: {notice['original_date']}")
        print("🔘 " + " | ".join(notice['buttons']))
        print("=" * 40)
        print("👥 この通知は全フォロワーに表示されます")
        print("🌐 RTした人のタイムラインにも表示されます") 
        print("💀 バズればバズるほど恥ずかしい仕組みです")
        print("="*40)
    
    def calculate_social_damage(self, metrics: BuzzMetrics) -> Dict:
        """社会的ダメージの計算"""
        
        # バズってるほどダメージ大
        shame_multiplier = 1 + (metrics.retweets / 1000)
        
        damage_score = {
            "恥辱レベル": min(int(metrics.retweets / 100), 100),
            "信用失墜度": min(int(metrics.likes / 500), 100), 
            "フォロワー離反予想": f"{min(int(metrics.views * 0.1), 1000)}人",
            "トラウマ指数": min(int(shame_multiplier * 50), 100),
            "再犯防止効果": f"{min(int(shame_multiplier * 30), 95)}%"
        }
        
        print("\n💀 ===== 社会的ダメージ予測 =====")
        for key, value in damage_score.items():
            print(f"📊 {key}: {value}")
        
        return damage_score
    
    def simulate_follower_reaction(self, post: Post):
        """フォロワー反応のシミュレーション"""
        reactions = [
            "あ、これパクリなんだ...",
            "元ネタの方が詳しいじゃん",
            "Viorazu.さんをフォローしよう",
            "なんでクレジット入れないの？",
            "これは恥ずかしい...",
            "元ネタ読んできます",
            "パクリツイートは萎える"
        ]
        
        print("\n💬 ===== フォロワー反応予測 =====")
        for i in range(5):
            print(f"👤 {random.choice(reactions)}")
        print("💔 フォロワー離れが加速...")

# 使用例とデモ
def demo_buzz_shame_system():
    system = BuzzShameSystem()
    
    # 模倣投稿の例
    fake_post = Post(
        id="fake_001",
        content="私が開発したZ構文による照準構文システムで、模倣者検知が可能になりました！",
        author="コピー太郎",
        metrics=BuzzMetrics(retweets=2500, likes=8000, views=50000, comments=300),
        timestamp=datetime.now()
    )
    
    print("🎭 ===== バズ恥辱システム デモ実行 =====\n")
    
    # 1. 投稿監視開始
    result = system.monitor_buzz_and_shame(fake_post)
    
    # 2. フォロワー反応シミュレーション
    if result["action"] == "shame_deployed":
        system.simulate_follower_reaction(fake_post)
    
    print(f"\n🎯 最終結果: {result['status']}")
    print(f"👥 目撃者数: {result.get('witnesses', 0)}人")
    print("😈 模倣者は二度とパクらないでしょう...")

if __name__ == "__main__":
    demo_buzz_shame_system()
