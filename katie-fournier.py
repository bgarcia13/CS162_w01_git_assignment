# Katie Fournier
# CS 162 Spring 2025
# Week 01
# Git Assignment


def rect_surface_area(length: int, width: int, height: int) -> int:
    return 2 * (rect_area(length, width) + rect_area(length, height) + rect_area(width, height))
