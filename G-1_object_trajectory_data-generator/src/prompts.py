"""Prompts and bilingual summaries for G-1 object trajectory."""

from __future__ import annotations


PROMPT_TEMPLATE_EN = (
    "The scene contains a {shape} object and a dashed target position "
    "(indicated by a dashed outline of the same shape). Keep the dashed "
    "target position unchanged. Move the {shape} object to the dashed "
    "target position along the shortest path, ensuring it completely "
    "overlaps with the target."
)


def get_prompt(task_type: str = "default", shape: str = "circle") -> str:
    return PROMPT_TEMPLATE_EN.format(shape=shape)


def get_task_summary_en() -> str:
    return (
        "Object trajectory: translate a single coloured shape (circle, square, "
        "triangle, or diamond) from its starting position to a dashed target "
        "outline of the same shape along the shortest straight-line path so "
        "that the moving shape perfectly overlaps the dashed target at the "
        "end. The dashed target stays static throughout."
    )


def get_task_summary_zh() -> str:
    return (
        "物体轨迹任务：将一个带颜色的形状（圆形、正方形、三角形或菱形）"
        "沿最短直线路径平移到一个虚线轮廓所标示的同形状目标位置，"
        "使其在终点处与虚线目标完全重合。虚线目标在整段动画中保持不动。"
    )


def get_rules_en() -> list[str]:
    return [
        "There is exactly one solid coloured shape and one dashed target "
        "outline of the same shape in the scene.",
        "The dashed target outline is static; only the solid shape moves.",
        "The solid shape translates along the shortest straight-line path "
        "from its starting centre to the target centre.",
        "The shape does not rotate, scale, or change colour during the motion.",
        "At the final frame the solid shape and dashed target completely overlap.",
    ]
