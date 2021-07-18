# README

## HTML

### Day 1

1. 市场分析
2. 内核
3. Web标准
    - 结构标准
    - 样式标准
    - 行为标准

**HTML** Hyper Text Markup Language

## webpack 

### QA

*网页中会引用哪些常见的静态资源*

- JS
- CSS
- Images
- Fonts
- 模板文件

*网页引入的静态资源多了，会带来的问题*

1. 网页加载速度慢，发起了很多的二次请求。
2. 处理错综复杂的依赖关系

*如何解决*

1. 合并、压缩、精灵图、图片的Base64编码
2. 使用`requireJS` `webpack`

*什么是webpack*

webpack是一个前端的项目构建工具，基于`Node.js`

*`Gulp`与`webpack`区别*

1. Gulp，基于Task任务
2. Webpack，基于项目构建



### 使用**webpack-dev-server**

1. 运行`webpack-dev-server` ，安装成项目的依赖
2. 安装完毕后，配置`start`命令于`package.json` （`webpack serve`）
3. `webpack.config.js` 里配置`devServer`参数