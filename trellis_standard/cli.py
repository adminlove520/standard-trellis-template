#!/usr/bin/env python
"""
trellis-standard CLI
Standard Trellis template initializer
"""

import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path
from typing import Optional


class Colors:
    """终端颜色"""
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GRAY = "\033[90m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def print_color(text: str, color: str = ""):
    """打印带颜色的文本"""
    print(f"{color}{text}{Colors.RESET}")


def get_template_dir() -> Path:
    """获取模板目录"""
    return Path(__file__).parent / "template"


def copy_template_files(source: Path, target: Path):
    """复制模板文件"""
    spec_source = source / "spec"
    spec_target = target / ".trellis" / "spec"

    if spec_source.exists():
        spec_target.mkdir(parents=True, exist_ok=True)
        for file in spec_source.glob("*.md"):
            shutil.copy2(file, spec_target / file.name)
            print_color(f"  ✓ {file.name}", Colors.GREEN)


def init_git(target: Path):
    """初始化 Git"""
    try:
        subprocess.run(["git", "init"], cwd=target, check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=target, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "feat: 初始化 Trellis 项目结构"],
            cwd=target,
            check=True,
            capture_output=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def init_trellis(target: Path, username: str) -> bool:
    """初始化 Trellis"""
    try:
        subprocess.run(
            ["trellis", "init", "-u", username],
            cwd=target,
            check=True,
            capture_output=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def create_project(
    name: str,
    username: str = "whoami",
    path: Optional[Path] = None,
    skip_git: bool = False
):
    """创建新项目"""
    if path is None:
        path = Path.cwd()

    project_path = path / name

    if project_path.exists():
        print_color(f"错误: 目录 {name} 已存在", Colors.RED)
        return False

    try:
        # 创建项目目录
        print_color("🚀 使用 Trellis 初始化项目", Colors.CYAN)
        print_color(f"项目名称: {name}", Colors.WHITE)
        print()

        project_path.mkdir(parents=True, exist_ok=True)

        # 初始化 Trellis
        print_color("📦 初始化 Trellis...", Colors.CYAN)
        if not init_trellis(project_path, username):
            print_color("  ⚠ Trellis 初始化失败，请确保已安装: npm install -g @mindfoldhq/trellis", Colors.YELLOW)

        # 复制规范模板
        print_color("📝 复制规范模板...", Colors.CYAN)
        template_dir = get_template_dir()
        if template_dir.exists():
            copy_template_files(template_dir, project_path)
        else:
            print_color("  ⚠ 模板目录未找到", Colors.YELLOW)

        # 复制 .gitignore
        gitignore_src = Path(__file__).parent.parent / ".gitignore"
        if gitignore_src.exists():
            shutil.copy2(gitignore_src, project_path / ".gitignore")

        # 初始化 Git
        if not skip_git:
            print_color("🔧 初始化 Git...", Colors.CYAN)
            if init_git(project_path):
                print_color("  ✓ Git 初始化成功", Colors.GREEN)
            else:
                print_color("  ⚠ Git 初始化失败", Colors.YELLOW)

        print()
        print_color("✅ 项目初始化完成！", Colors.GREEN)
        print()
        print_color("📋 下一步:", Colors.CYAN)
        print_color(f"  1. cd {name}", Colors.WHITE)
        print_color("  2. 开始与 AI 头脑风暴，定义你的 PRD", Colors.WHITE)
        print_color("  3. AI 会自动调用 trellis-implement 开始实现", Colors.WHITE)
        print()
        print_color("💡 提示:", Colors.CYAN)
        print_color("  - 规范文件位于 .trellis/spec/", Colors.WHITE)
        print_color("  - 可根据项目需求修改规范", Colors.WHITE)
        print_color("  - 团队成员可直接 clone 并开始协作", Colors.WHITE)

        return True

    except Exception as e:
        print_color(f"错误: {e}", Colors.RED)
        return False


def main():
    """CLI 入口"""
    parser = argparse.ArgumentParser(
        description="Standard Trellis Template - AI 编码工程化标准模板",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  trellis-init-standard my-project
  trellis-init-standard my-project --username your-name
  trellis-init-standard my-project --path /path/to/projects
        """
    )
    parser.add_argument(
        "name",
        help="项目名称"
    )
    parser.add_argument(
        "-u", "--username",
        default="whoami",
        help="用户名 (默认: whoami)"
    )
    parser.add_argument(
        "-p", "--path",
        type=Path,
        help="项目路径 (默认: 当前目录)"
    )
    parser.add_argument(
        "--skip-git",
        action="store_true",
        help="跳过 Git 初始化"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"trellis-standard-template {__version__}"
    )

    args = parser.parse_args()

    print()
    print_color("🌳 Standard Trellis Template", Colors.CYAN)
    print_color("AI 编码工程化标准模板", Colors.GRAY)
    print()

    success = create_project(
        name=args.name,
        username=args.username,
        path=args.path,
        skip_git=args.skip_git
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
