#!/usr/bin/env node

/**
 * create-trellis-standard
 * Standard Trellis template initializer
 */

const fs = require('fs-extra');
const path = require('path');
const chalk = require('chalk');
const ora = require('ora');
const prompts = require('prompts');

const TEMPLATE_DIR = path.join(__dirname, '..', '.trellis-template');

async function main() {
  console.log();
  console.log(chalk.cyan.bold('🌳 Standard Trellis Template'));
  console.log(chalk.gray('AI 编码工程化标准模板初始化器\n'));

  const response = await prompts([
    {
      type: 'text',
      name: 'projectName',
      message: '项目名称',
      initial: 'my-project',
      validate: (name) => name.trim() !== '' || '项目名称不能为空'
    },
    {
      type: 'text',
      name: 'username',
      message: '你的名字',
      initial: 'whoami',
      validate: (name) => name.trim() !== '' || '名字不能为空'
    },
    {
      type: 'select',
      name: 'platform',
      message: '选择平台',
      choices: [
        { title: '全部平台', value: 'all' },
        { title: 'Claude Code', value: 'claude' },
        { title: 'OpenClaw', value: 'openclaw' },
        { title: 'Hermes', value: 'hermes' },
        { title: 'Cursor', value: 'cursor' }
      ],
      initial: 0
    }
  ]);

  if (!response.projectName) {
    console.log(chalk.yellow('操作已取消'));
    process.exit(0);
  }

  const { projectName, username, platform } = response;
  const targetDir = path.resolve(process.cwd(), projectName);

  // 检查目录是否已存在
  if (await fs.pathExists(targetDir)) {
    console.log(chalk.red(`目录 ${projectName} 已存在`));
    process.exit(1);
  }

  try {
    // 创建项目目录
    const createSpinner = ora('创建项目目录').start();
    await fs.ensureDir(targetDir);
    createSpinner.succeed();

    // 初始化 Trellis
    const trellisSpinner = ora('初始化 Trellis').start();
    const { execSync } = require('child_process');
    try {
      execSync(`trellis init -u ${username}`, {
        cwd: targetDir,
        stdio: 'ignore'
      });
    } catch (e) {
      trellisSpinner.warn('Trellis 初始化失败，请确保已安装: npm install -g @mindfoldhq/trellis');
    }
    trellisSpinner.succeed();

    // 复制规范模板
    const specSpinner = ora('复制规范模板').start();
    const specSource = path.join(__dirname, '..', '.trellis-template', 'spec');
    const specTarget = path.join(targetDir, '.trellis', 'spec');

    if (await fs.pathExists(specSource)) {
      await fs.ensureDir(specTarget);
      await fs.copy(specSource, specTarget);
    }
    specSpinner.succeed();

    // 复制 .gitignore
    const gitignoreSource = path.join(__dirname, '..', '.gitignore');
    const gitignoreTarget = path.join(targetDir, '.gitignore');

    if (await fs.pathExists(gitignoreSource)) {
      await fs.copy(gitignoreSource, gitignoreTarget);
    }

    // 复制 README
    const readmeSource = path.join(__dirname, '..', 'PROJECT_README.md');
    const readmeTarget = path.join(targetDir, 'README.md');

    if (await fs.pathExists(readmeSource)) {
      let readme = await fs.readFile(readmeSource, 'utf-8');
      readme = readme.replace(/\{PROJECT_NAME\}/g, projectName);
      await fs.writeFile(readmeTarget, readme);
    }

    // 初始化 Git
    const gitSpinner = ora('初始化 Git').start();
    try {
      execSync('git init', { cwd: targetDir, stdio: 'ignore' });
      execSync('git add .', { cwd: targetDir, stdio: 'ignore' });
      execSync('git commit -m "feat: 初始化 Trellis 项目结构"', {
        cwd: targetDir,
        stdio: 'ignore'
      });
    } catch (e) {
      gitSpinner.warn('Git 初始化失败');
    }
    gitSpinner.succeed();

    console.log();
    console.log(chalk.green.bold('✅ 项目初始化完成！\n'));
    console.log(chalk.cyan('📋 下一步:\n'));
    console.log(chalk.white(`  1. cd ${projectName}`));
    console.log(chalk.white('  2. 开始与 AI 头脑风暴，定义你的 PRD'));
    console.log(chalk.white('  3. AI 会自动调用 trellis-implement 开始实现\n'));
    console.log(chalk.cyan('💡 提示:\n'));
    console.log(chalk.white('  - 规范文件位于 .trellis/spec/'));
    console.log(chalk.white('  - 可根据项目需求修改规范'));
    console.log(chalk.white('  - 团队成员可直接 clone 并开始协作\n'));

  } catch (error) {
    console.error(chalk.red('初始化失败:', error.message));
    process.exit(1);
  }
}

main();
