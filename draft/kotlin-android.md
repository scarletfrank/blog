# README

## basic-android-kotlin-training

### 1

- [playground](https://developer.android.com/training/kotlinplayground) 是一个网页版交互式代码编辑器，您可以在其中练习编写 Kotlin 程序。
- 所有 Kotlin 程序都需要有一个 `main()` 函数：`fun main() {}`
- `println()` 函数用于输出一行文本。
- 用双引号括住您要输出的文本。例如 `"Hello"`。
- 重复 `println()` 指令可输出多行文本。
- 程序中的错误会标记为红色。输出窗格中会显示错误消息来帮助您确定发生错误的位置以及错误原因。

### 2

- 使用 `${}` 将输出语句的文本中的变量和计算括起来。例如：`${age}`，其中的 `age` 就是变量。
- 使用 val 关键字和名称创建变量。此值设定后即无法更改。使用等号为变量赋值。值的示例包括文本和数字。
- `String` 是用引号括起来的文本，例如 `"Hello"`。
- `Int` 是正整数或负整数，例如 0、23 或 -1024。
- 您可以将一个或多个参数传入函数中供函数使用，例如：`fun printCakeBottom(age:Int, layers:Int) {}`
- 使用 `repeat() {}` 语句重复一组指令若干次。例如，`repeat (23) { print("%") }` 或 `repeat (layers) { print("@@@@@@@@@@") }`
- 循环是用于多次重复某指令的一个指令。`repeat()` 语句就是循环的一个示例。
- 您可以嵌套循环，即，将循环放到循环内。例如，您可以在 `repeat()` 语句内创建一个 `repeat()` 语句，用于将符号输出若干次和若干行，就像您对蛋糕层所做的那样。

有关函数参数用法的摘要：如需使用包含参数的函数，您需要执行以下三项操作：

- 将参数和类型添加到函数定义中：`printBorder(border: String)`
- 在函数内使用参数：`println(border)`
- 在调用函数时提供参数：`printBorder(border)`

### 3

- 如要创建新项目，请启动 Android Studio，点击 + Start a new Android Studio project，为项目命名，选择模板，然后填写详细信息。
- 如要创建 Android 虚拟设备（模拟器）来运行应用，请依次选择 Tools > AVD Manager，然后使用 AVD 管理器选择硬件设备和系统映像。
-如要在虚拟设备上运行应用，请确保您已创建设备，从工具栏下拉菜单中选择相应设备，然后点击工具栏中的 Run 图标 依次选择“Run”>“Run app”，或点击工具栏中的“Run”图标 [ICON HERE]。[IMAGEINFO]：ic_run.png，Android Studio 的“Run”图标 以运行您的应用。
- 如要查找项目文件，请转到 Project 窗口，从下拉列表中选择 Project Source Files。

### 4

- 布局编辑器可帮助您创建 Android 应用的界面。
- 您在应用屏幕上看到的所有内容几乎均属于 View。
- TextView 是在应用中显示文本的界面元素。
- ConstraintLayout 是存放其他界面元素的容器。
- 在 ConstraintLayout 中，必须为 Views 设置水平和垂直方向的约束条件。
- 放置 View 的一种方式是使用外边距。
- 外边距表示 View 离它所处容器的边缘有多远。
- 您可以在 TextView 上设置字体、文字大小和颜色等属性。