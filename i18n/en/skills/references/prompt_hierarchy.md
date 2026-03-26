# Prompt Hierarchy Reference (Prompt Hierarchy Reference)

本文件定义了干预切片中常用的标准prompt hierarchy（Least to Most 或 Most to Least）。
当执行 `program-slicer` 需要给出“初始辅助”和“目标prompt fading梯队”时，请参考以下层级名称，**切勿自编无关术语**。

## 一、基础能力/动作类（全辅助切片）
* **全物理辅助 (Full Physical)**：手把手带领儿童完成全部动作（如手把手将积木放入卡槽）。
* **部分物理辅助 (Partial Physical)**：仅在儿童的手腕或手肘处给予轻触引导（如轻推手肘）。
* **模型辅助 (Modeling)**：治疗师示范一次完整的动作，让儿童模仿（如“看我怎么做”）。
* **手势辅助 (Gestural)**：治疗师用手指指向目标物，或用眼神注视目标物（Point / Look）。
* **位置辅助 (Positional)**：将正确答案卡片放在离儿童最近的地方。
* **口头/视觉线索辅助 (Verbal / Visual Cue)**：不直接给出答案，而是给规律提示（如“它是红色的”或拿出一张提醒卡）。
* **独立 (Independent/Mastered)**：发出 SD 后，无须任何辅助，规定延迟时间内（通常为 3 秒以内）准确回应。

## 二、发音/言语类 (Echoic to XXX Transfer)
* **全口头辅助 (Full Verbal)**：直接说出答案让儿童仿说（如问“这是什么”马上接“苹果”）。
* **部分口头辅助/首音辅助 (Partial Verbal)**：只给出答案的第一个音节（如问“这是什么”马上接“苹...”）。
* **发音嘴型辅助 (Articulation / Mouth Positional)**：不发声，但做出第一个音节的夸张嘴型让儿童观察。
* **独立发音 (Independent)**：发出 SD 或面临 MO 时，自然说出目标语音。

## 三、Fading Rules (Fading Rule)
- 错误纠正时（Error Correction）：通常使用从高到低（Most to Least），确保正确率，减少挫败感。
- 探测维持时（Probing）：通常使用从低到高（Least to Most），给予儿童独立思考的机会（如 3 秒延迟）。
