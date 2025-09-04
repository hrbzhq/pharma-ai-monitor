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