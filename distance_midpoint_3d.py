import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def midpoint(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)

def plot_3d(p1, p2):
    dist = distance(p1, p2)
    mid = midpoint(p1, p2)
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    mx, my, mz = mid
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot([x1, x2], [y1, y2], [z1, z2], 'b-', linewidth=2, alpha=0.6)
    ax.scatter(x1, y1, z1, c='r', s=100, label=f'P1: ({x1}, {y1}, {z1})')
    ax.scatter(x2, y2, z2, c='g', s=100, label=f'P2: ({x2}, {y2}, {z2})')
    ax.scatter(mx, my, mz, c='m', s=100, label=f'Mid: ({mx:.2f}, {my:.2f}, {mz:.2f})')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Distance & Midpoint')
    ax.legend()
    
    info = f'Distance: {dist:.4f}\nMidpoint: ({mx:.4f}, {my:.4f}, {mz:.4f})'
    ax.text2D(0.02, 0.98, info, transform=ax.transAxes,
              bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
              verticalalignment='top', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Distance: {dist:.4f}")
    print(f"Midpoint: ({mx:.4f}, {my:.4f}, {mz:.4f})")

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (5, 7, 9)
    plot_3d(point1, point2)

