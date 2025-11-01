                                      ##============##
                                      ##-Panim_1.py-##
                                      ##============##
################################################################################################
## Features:                                                                                  ##
##--------------------------------------------------------------------------------------------##
## Triple-layer orbital flow – inner core, mid-arms, and outer drift all move independently.  ##
##============================================================================================##
## Continuous RGB hue cycling – true smooth color blending with sine-based offsets.           ##
##============================================================================================##
## Volumetric depth – brightness fades by “distance,” simulating a real 3D galaxy.            ##
##============================================================================================##
## Core plasma pulse – the galactic center throbs with energy waves.                          ##
##============================================================================================##
## Procedural star flicker – subtle random glints across the arms.                            ##
##============================================================================================##
## Perfectly smooth motion – cursor repositioning, no flicker, optimized for terminals.       ##
################################################################################################

import os, sys, math, time, random

# Hide cursor and clear once
sys.stdout.write("\033[2J\033[?25l")
sys.stdout.flush()

RESET = "\033[0m"

width, height = 120, 35
t = 0.0

def move_cursor_top():
    sys.stdout.write("\033[H")
    sys.stdout.flush()

def hsv_to_rgb(h):
    h = h % 1.0
    i = int(h * 6)
    f = h * 6 - i
    q = int(255 * (1 - f))
    t = int(255 * f)
    if i == 0: r, g, b = 255, t, 0
    elif i == 1: r, g, b = q, 255, 0
    elif i == 2: r, g, b = 0, 255, t
    elif i == 3: r, g, b = 0, q, 255
    elif i == 4: r, g, b = t, 0, 255
    else: r, g, b = 255, 0, q
    return r, g, b

def ansi_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

coords = [(x, y) for y in range(-height//2, height//2)
                for x in range(-width//2, width//2)]

try:
    while True:
        move_cursor_top()
        frame = []
        # Core pulsation and layer rotations
        core_pulse = 1.0 + 0.3 * math.sin(t * 0.8)
        inner_spin = t * 0.07
        mid_spin = t * 0.05
        outer_spin = t * 0.02
        hue_base = (math.sin(t * 0.1) + 1) / 2

        for y in range(-height//2, height//2):
            row = []
            for x in range(-width//2, width//2):
                r = math.sqrt(x**2 + y**2)
                a = math.atan2(y, x)

                # Three rotational layers
                if r < 10:
                    rot = a + inner_spin
                    layer_speed = 3.2
                elif r < 20:
                    rot = a + mid_spin
                    layer_speed = 2.4
                else:
                    rot = a + outer_spin
                    layer_speed = 1.6

                s = math.sin(rot * layer_speed + r / 3)
                c = math.cos(rot * (layer_speed / 2) - r / 4)
                brightness = (s + c + 2) / 4

                swirl_limit = (math.sin(t * 0.7) + 2.3) * 13
                if r < swirl_limit:
                    # 3D depth shading
                    depth = 1.0 - (r / swirl_limit) ** 1.4
                    hue = (hue_base + r / 60 + rot / 8) % 1.0
                    r_col, g_col, b_col = hsv_to_rgb(hue)
                    # fade color by depth
                    r_col = int(r_col * depth)
                    g_col = int(g_col * depth)
                    b_col = int(b_col * depth)
                    color = ansi_color(r_col, g_col, b_col)

                    # Core glow (super bright)
                    if r < 3 * core_pulse:
                        intensity = 0.8 + 0.2 * math.sin(t * 4 + r)
                        r_glow = int(255 * intensity)
                        g_glow = int(200 * intensity)
                        b_glow = int(160 * intensity)
                        color = ansi_color(r_glow, g_glow, b_glow)
                        char = random.choice(["✶", "✦", "*"])
                    else:
                        # choose brightness symbol
                        chars = " .·•*✶✦"
                        idx = min(int(brightness * len(chars)), len(chars)-1)
                        char = chars[idx]
                        # random shimmer
                        if random.random() < 0.015:
                            char = random.choice([".", "·", "•", "*"])
                    row.append(f"{color}{char}{RESET}")
                else:
                    row.append(" ")
            frame.append("".join(row))

        print("\n".join(frame))
        t += 0.12
        time.sleep(0.03)

except KeyboardInterrupt:
    sys.stdout.write("\033[?25h" + RESET + "\n🌌 Singularity Pulse ended 🌌\n")
