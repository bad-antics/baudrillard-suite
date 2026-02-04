#!/usr/bin/env python3
"""
SIMULACRA - Image Reality Distortion Engine
============================================
"The simulacrum is never that which conceals the truth—
it is the truth which conceals that there is none."
— Jean Baudrillard

Transforms images through layers of hyperreal manipulation,
creating copies without originals.
"""

import os
import sys
import random
import argparse
from pathlib import Path

try:
    from PIL import Image, ImageFilter, ImageEnhance, ImageOps
    import numpy as np
except ImportError:
    print("Install: pip install pillow numpy")
    sys.exit(1)

BANNER = """
███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗  ██████╗██████╗  █████╗ 
██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗
███████╗██║██╔████╔██║██║   ██║██║     ███████║██║     ██████╔╝███████║
╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║██║     ██╔══██╗██╔══██║
███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║╚██████╗██║  ██║██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
        [ IMAGE REALITY DISTORTION | baudrillard-suite ]
"""

class SimulacraEngine:
    """Transform reality through orders of simulacra"""
    
    def __init__(self, image_path):
        self.original = Image.open(image_path)
        self.current = self.original.copy()
        self.order = 0  # Current order of simulacra
        
    def first_order(self):
        """Reflection of basic reality - subtle distortion"""
        # Slight color shift, minor blur
        enhancer = ImageEnhance.Color(self.current)
        self.current = enhancer.enhance(1.15)
        self.current = self.current.filter(ImageFilter.GaussianBlur(radius=0.5))
        self.order = 1
        return self
        
    def second_order(self):
        """Masks and perverts basic reality"""
        # More aggressive manipulation
        self.current = ImageOps.posterize(self.current, 6)
        enhancer = ImageEnhance.Contrast(self.current)
        self.current = enhancer.enhance(1.3)
        self.order = 2
        return self
        
    def third_order(self):
        """Masks the absence of basic reality"""
        # Heavy stylization
        self.current = self.current.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.current = ImageOps.solarize(self.current, threshold=128)
        self.order = 3
        return self
        
    def fourth_order(self):
        """Pure simulacrum - no relation to reality"""
        # Complete transformation
        arr = np.array(self.current)
        # Channel swap
        if len(arr.shape) == 3:
            arr = arr[:, :, ::-1]  # RGB -> BGR
        # Add noise
        noise = np.random.randint(-30, 30, arr.shape, dtype=np.int16)
        arr = np.clip(arr.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        self.current = Image.fromarray(arr)
        self.current = self.current.filter(ImageFilter.FIND_EDGES)
        self.order = 4
        return self
        
    def hyperreal(self):
        """More real than real - the hyperreal"""
        # Excessive sharpening and saturation
        enhancer = ImageEnhance.Sharpness(self.current)
        self.current = enhancer.enhance(3.0)
        enhancer = ImageEnhance.Color(self.current)
        self.current = enhancer.enhance(2.0)
        return self
        
    def precession(self):
        """The precession of simulacra - recursive copies"""
        # Create ghost images
        layers = []
        for i in range(3):
            layer = self.current.copy()
            layer = layer.rotate(i * 2, expand=False)
            layers.append(layer)
        
        result = Image.blend(layers[0], layers[1], 0.5)
        result = Image.blend(result, layers[2], 0.3)
        self.current = result
        return self
        
    def save(self, output_path):
        """Save the simulacrum"""
        self.current.save(output_path)
        print(f"[SIMULACRA] Order {self.order} saved: {output_path}")
        
    def get_order_description(self):
        descriptions = {
            0: "Original - basic reality",
            1: "First Order - reflection of basic reality",
            2: "Second Order - masks and perverts basic reality", 
            3: "Third Order - masks the absence of basic reality",
            4: "Fourth Order - pure simulacrum, no relation to reality"
        }
        return descriptions.get(self.order, "Unknown order")


def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description="Simulacra - Image Reality Distortion Engine"
    )
    parser.add_argument("image", help="Input image path")
    parser.add_argument("-o", "--output", help="Output path", default="simulacrum.png")
    parser.add_argument("--order", type=int, choices=[1,2,3,4], default=4,
                       help="Order of simulacra (1-4)")
    parser.add_argument("--hyperreal", action="store_true",
                       help="Apply hyperreal enhancement")
    parser.add_argument("--precession", action="store_true",
                       help="Apply precession effect")
    parser.add_argument("--all", action="store_true",
                       help="Generate all orders")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.image):
        print(f"[ERROR] Image not found: {args.image}")
        sys.exit(1)
        
    if args.all:
        # Generate all orders
        base = Path(args.output).stem
        ext = Path(args.output).suffix or ".png"
        
        for order in range(1, 5):
            engine = SimulacraEngine(args.image)
            for o in range(1, order + 1):
                getattr(engine, ["", "first_order", "second_order", 
                                "third_order", "fourth_order"][o])()
            
            if args.hyperreal:
                engine.hyperreal()
            if args.precession:
                engine.precession()
                
            output = f"{base}_order{order}{ext}"
            engine.save(output)
            print(f"  → {engine.get_order_description()}")
    else:
        engine = SimulacraEngine(args.image)
        
        # Apply orders progressively
        for o in range(1, args.order + 1):
            getattr(engine, ["", "first_order", "second_order",
                            "third_order", "fourth_order"][o])()
        
        if args.hyperreal:
            engine.hyperreal()
        if args.precession:
            engine.precession()
            
        engine.save(args.output)
        print(f"\n  → {engine.get_order_description()}")


if __name__ == "__main__":
    main()
