#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
药企AI需求监控系统 - 独立服务器版本
完全独立，不依赖其他模块
"""

import os
import logging
import sqlite3
import json
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, jsonify, request

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_standalone_app():
    """创建独立的Flask应用"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'pharma-ai-monitor-standalone'
    
    # 定义数据库路径
    current_dir = Path(__file__).parent
    db_path = current_dir / 'database' / 'pharma_ai.db'
    db_path.parent.mkdir(exist_ok=True)
    
    @app.route('/')
    def index():
        """主页"""
        try:
            return render_template('index.html')
        except Exception as e:
            # 如果模板不存在，返回简单的HTML
            return f"""
            <!DOCTYPE html>
            <html lang="zh-CN">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>药企AI需求监控系统</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
                <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            </head>
            <body class="bg-light">
                <div class="container my-5">
                    <div class="row">
                        <div class="col-12 text-center">
                            <h1 class="display-4 text-primary mb-4">
                                <i class="fas fa-pills me-3"></i>药企AI需求监控系统
                            </h1>
                            <p class="lead text-muted">实时监控全球药企AI需求，智能分析就业机会</p>
                        </div>
                    </div>
                    
                    <div class="row g-4 mt-4">
                        <div class="col-md-4">
                            <div class="card h-100 shadow-sm">
                                <div class="card-body text-center">
                                    <i class="fas fa-search fa-3x text-primary mb-3"></i>
                                    <h5 class="card-title">AI需求监控</h5>
                                    <p class="card-text">自动收集和分析药企AI项目需求</p>
                                    <a href="/api/requirements" class="btn btn-primary">查看需求</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-md-4">
                            <div class="card h-100 shadow-sm">
                                <div class="card-body text-center">
                                    <i class="fas fa-chart-bar fa-3x text-success mb-3"></i>
                                    <h5 class="card-title">数据分析</h5>
                                    <p class="card-text">深度分析AI需求趋势和市场动向</p>
                                    <a href="/api/stats" class="btn btn-success">查看统计</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-md-4">
                            <div class="card h-100 shadow-sm">
                                <div class="card-body text-center">
                                    <i class="fas fa-briefcase fa-3x text-warning mb-3"></i>
                                    <h5 class="card-title">就业推荐</h5>
                                    <p class="card-text">基于AI分析的个性化职位推荐</p>
                                    <a href="/api/jobs" class="btn btn-warning">查看职位</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="row mt-5">
                        <div class="col-12">
                            <div class="card">
                                <div class="card-header bg-primary text-white">
                                    <h5 class="mb-0"><i class="fas fa-info-circle me-2"></i>系统状态</h5>
                                </div>
                                <div class="card-body">
                                    <div class="row text-center">
                                        <div class="col-md-3">
                                            <h3 class="text-primary">15</h3>
                                            <small class="text-muted">监控需求</small>
                                        </div>
                                        <div class="col-md-3">
                                            <h3 class="text-success">8</h3>
                                            <small class="text-muted">合作药企</small>
                                        </div>
                                        <div class="col-md-3">
                                            <h3 class="text-warning">12</h3>
                                            <small class="text-muted">就业机会</small>
                                        </div>
                                        <div class="col-md-3">
                                            <h3 class="text-info">在线</h3>
                                            <small class="text-muted">系统状态</small>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
            """
    
    @app.route('/api/requirements')
    def get_requirements():
        """获取AI需求列表"""
        sample_requirements = [
            {
                'id': 1,
                'company': 'Pfizer',
                'title': 'AI Drug Discovery Platform',
                'description': '开发基于AI的药物发现平台，加速新药研发过程',
                'category': 'Drug Discovery',
                'urgency': 'high',
                'budget': '$2M-5M',
                'location': '上海',
                'skills': ['Deep Learning', 'Bioinformatics', 'Python'],
                'created_at': '2025-09-03'
            },
            {
                'id': 2,
                'company': 'AstraZeneca',
                'title': 'Clinical Trial Optimization',
                'description': '使用AI优化临床试验设计和患者招募流程',
                'category': 'Clinical Analytics',
                'urgency': 'medium',
                'budget': '$1M-3M',
                'location': '北京',
                'skills': ['Machine Learning', 'Statistics', 'Clinical Research'],
                'created_at': '2025-09-02'
            },
            {
                'id': 3,
                'company': 'GSK',
                'title': 'AI-Powered Vaccine Development',
                'description': 'AI辅助疫苗研发和效果预测系统',
                'category': 'Vaccine Research',
                'urgency': 'high',
                'budget': '$3M-8M',
                'location': '广州',
                'skills': ['Computer Vision', 'Immunology', 'Deep Learning'],
                'created_at': '2025-09-01'
            },
            {
                'id': 4,
                'company': 'Eli Lilly',
                'title': 'Personalized Medicine AI',
                'description': '个性化医疗AI解决方案开发',
                'category': 'Personalized Medicine',
                'urgency': 'medium',
                'budget': '$1.5M-4M',
                'location': '深圳',
                'skills': ['Genomics AI', 'Machine Learning', 'Biomarkers'],
                'created_at': '2025-08-31'
            },
            {
                'id': 5,
                'company': 'Novartis',
                'title': 'AI Drug Safety Monitoring',
                'description': 'AI驱动的药物安全监测和不良反应检测',
                'category': 'Drug Safety',
                'urgency': 'high',
                'budget': '$800K-2M',
                'location': '苏州',
                'skills': ['NLP', 'Anomaly Detection', 'Healthcare Data'],
                'created_at': '2025-08-30'
            }
        ]
        
        return jsonify({
            'success': True,
            'data': sample_requirements,
            'total': len(sample_requirements)
        })
    
    @app.route('/api/stats')
    def get_stats():
        """获取统计信息"""
        stats = {
            'total_requirements': 15,
            'total_companies': 8,
            'total_jobs': 12,
            'high_urgency': 8,
            'categories': {
                'Drug Discovery': 5,
                'Clinical Analytics': 3,
                'Vaccine Research': 2,
                'Personalized Medicine': 3,
                'Drug Safety': 2
            },
            'top_skills': [
                {'skill': 'Machine Learning', 'count': 12},
                {'skill': 'Deep Learning', 'count': 8},
                {'skill': 'Python', 'count': 10},
                {'skill': 'NLP', 'count': 6},
                {'skill': 'Computer Vision', 'count': 4}
            ],
            'budget_distribution': {
                '<$1M': 2,
                '$1M-3M': 6,
                '$3M-5M': 4,
                '>$5M': 3
            }
        }
        
        return jsonify({
            'success': True,
            'data': stats
        })
    
    @app.route('/api/jobs')
    def get_jobs():
        """获取就业推荐"""
        sample_jobs = [
            {
                'id': 1,
                'company': 'Pfizer',
                'position': '高级AI药物发现科学家',
                'job_type': 'full-time',
                'location': '上海',
                'salary_range': '$150K-200K',
                'skills_required': '["Deep Learning", "Drug Discovery", "Python", "TensorFlow"]',
                'match_score': 0.92,
                'recommendation_reason': '基于您的AI和药物发现背景，这个职位非常匹配',
                'created_at': '2025-09-03'
            },
            {
                'id': 2,
                'company': 'AstraZeneca',
                'position': '临床数据科学家',
                'job_type': 'full-time',
                'location': '北京',
                'salary_range': '$120K-160K',
                'skills_required': '["Machine Learning", "Statistics", "Clinical Research"]',
                'match_score': 0.85,
                'recommendation_reason': '临床AI应用领域的优秀机会',
                'created_at': '2025-09-02'
            },
            {
                'id': 3,
                'company': 'GSK',
                'position': 'AI疫苗研发工程师',
                'job_type': 'contract',
                'location': '广州',
                'salary_range': '$140K-190K',
                'skills_required': '["Computer Vision", "Immunology", "Deep Learning"]',
                'match_score': 0.88,
                'recommendation_reason': '疫苗AI研发的前沿项目',
                'created_at': '2025-09-01'
            },
            {
                'id': 4,
                'company': 'Eli Lilly',
                'position': '个性化医疗AI专家',
                'job_type': 'full-time',
                'location': '深圳',
                'salary_range': '$130K-180K',
                'skills_required': '["Machine Learning", "Genomics", "Python", "R"]',
                'match_score': 0.82,
                'recommendation_reason': '个性化医疗AI的创新应用机会',
                'created_at': '2025-08-31'
            },
            {
                'id': 5,
                'company': 'Novartis',
                'position': 'AI药物安全监测工程师',
                'job_type': 'remote',
                'location': '远程',
                'salary_range': '$110K-150K',
                'skills_required': '["NLP", "Anomaly Detection", "Python", "Healthcare"]',
                'match_score': 0.79,
                'recommendation_reason': '药物安全AI监测的重要岗位',
                'created_at': '2025-08-30'
            }
        ]
        
        return jsonify({
            'success': True,
            'data': sample_jobs,
            'total': len(sample_jobs)
        })
    
    @app.route('/api/scheduler/status')
    def scheduler_status():
        """调度器状态API - 独立版本"""
        return jsonify({
            'success': True,
            'data': {
                'running': False,
                'status': 'disabled',
                'message': '独立版本未启用自动调度器',
                'last_run': None,
                'next_run': None,
                'jobs': []
            }
        })
    
    @app.route('/favicon.ico')
    def favicon():
        """处理favicon请求，避免404"""
        return '', 204
    
    @app.route('/test')
    def test():
        """测试页面"""
        return """
        <html>
        <head>
            <title>测试页面</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-header bg-success text-white">
                                <h3><i class="fas fa-check-circle"></i> 药企AI需求监控系统测试页面</h3>
                            </div>
                            <div class="card-body">
                                <div class="alert alert-success">
                                    <h4>✅ 服务器运行正常！</h4>
                                </div>
                                <div class="row">
                                    <div class="col-md-6">
                                        <h5>API端点测试：</h5>
                                        <ul class="list-group">
                                            <li class="list-group-item">
                                                <a href="/api/requirements" class="btn btn-sm btn-primary">需求API</a>
                                                <span class="ms-2">获取药企AI需求</span>
                                            </li>
                                            <li class="list-group-item">
                                                <a href="/api/stats" class="btn btn-sm btn-success">统计API</a>
                                                <span class="ms-2">获取统计信息</span>
                                            </li>
                                            <li class="list-group-item">
                                                <a href="/api/jobs" class="btn btn-sm btn-warning">职位API</a>
                                                <span class="ms-2">获取就业推荐</span>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="col-md-6">
                                        <h5>页面导航：</h5>
                                        <ul class="list-group">
                                            <li class="list-group-item">
                                                <a href="/" class="btn btn-sm btn-outline-primary">返回主页</a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    
    return app

if __name__ == "__main__":
    print("🚀 启动药企AI需求监控系统 (独立版)")
    print("=" * 50)
    
    try:
        app = create_standalone_app()
        print("✅ 应用初始化完成")
        print("🌐 启动Web服务器...")
        print("📱 访问地址:")
        print("   - 主页: http://localhost:5000")
        print("   - 测试页: http://localhost:5000/test")
        print("   - API需求: http://localhost:5000/api/requirements")
        print("   - API统计: http://localhost:5000/api/stats")
        print("   - API职位: http://localhost:5000/api/jobs")
        print("🛑 按 Ctrl+C 停止服务")
        print("=" * 50)
        
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True
        )
        
    except Exception as e:
        logger.error(f"启动失败: {e}")
        print(f"❌ 启动失败: {e}")