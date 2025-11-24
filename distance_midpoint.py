import matplotlib.pyplot as plt
import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def plot_2d(p1, p2):
    dist = distance(p1, p2)
    mid = midpoint(p1, p2)
    x1, y1 = p1
    x2, y2 = p2
    mx, my = mid
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot([x1, x2], [y1, y2], 'b-', linewidth=2, alpha=0.6)
    ax.plot(x1, y1, 'ro', markersize=10, label=f'P1: ({x1}, {y1})')
    ax.plot(x2, y2, 'go', markersize=10, label=f'P2: ({x2}, {y2})')
    ax.plot(mx, my, 'mo', markersize=10, label=f'Mid: ({mx:.2f}, {my:.2f})')
    
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('2D Distance & Midpoint')
    ax.set_aspect('equal')
    ax.legend()
    
    info = f'Distance: {dist:.4f}\nMidpoint: ({mx:.4f}, {my:.4f})'
    ax.text(0.02, 0.98, info, transform=ax.transAxes, 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
            verticalalignment='top', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Distance: {dist:.4f}")
    print(f"Midpoint: ({mx:.4f}, {my:.4f})")

if __name__ == "__main__":
    point1 = (2, 3)
    point2 = (8, 10)
    plot_2d(point1, point2)

