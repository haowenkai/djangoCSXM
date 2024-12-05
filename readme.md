# 智慧物业管理平台

## 项目简介

智慧物业管理平台是一个用于管理物业、业主和财务的综合系统。该平台提供了多种功能模块，包括房屋业主管理、财务管理、报表管理等，帮助物业公司高效地管理日常事务。

## 功能模块

- **首页**: 提供物业数量、小区数量、业主总数等统计信息的概览。
- **房屋业主管理**: 管理房屋和业主信息。
- **财务管理**: 管理财务收支和账单。
- **报表管理**: 生成和查看各种报表。
- **报事报修**: 处理业主的报修请求。
- **宣传公告**: 发布和管理公告信息。
- **物业管理**: 管理物业的日常运营。
- **权限管理**: 管理用户权限和角色。

## 技术栈

- **后端**: Django
- **前端**: Bootstrap, Chart.js
- **数据库**: SQLite (可根据需求更换为其他数据库)

## 安装与运行

1. 克隆项目到本地：
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. 创建并激活虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 使用 `venv\Scripts\activate`
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```

5. 启动开发服务器：
   ```bash
   python manage.py runserver
   ```

6. 在浏览器中访问 `http://127.0.0.1:8000/` 查看项目。

## 贡献

欢迎贡献代码！请提交 Pull Request 或报告 Issue。

## 许可证

该项目遵循 MIT 许可证。
