import matplotlib.pyplot as plt
import numpy as np

def plot_trajectories(positions, title="Pedestrian Trajectories"):
    """Plot pedestrian trajectories."""
    plt.figure(figsize=(10, 8))
    for ped_id, traj in positions.items():
        traj = np.array(traj)
        plt.plot(traj[:, 0], traj[:, 1], label=f"Ped {ped_id}")
    plt.title(title)
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

def animate_trajectories(positions, output_file="animation.mp4"):
    """Animate pedestrian trajectories (requires ffmpeg)."""
    import matplotlib.animation as animation
    fig, ax = plt.subplots(figsize=(10, 8))
    trajectories = {k: np.array(v) for k, v in positions.items()}
    n_frames = max(len(traj) for traj in trajectories.values())
    
    def update(frame):
        ax.clear()
        for ped_id, traj in trajectories.items():
            if frame < len(traj):
                ax.plot(traj[:frame+1, 0], traj[:frame+1, 1], label=f"Ped {ped_id}")
                ax.scatter(traj[frame, 0], traj[frame, 1], s=50)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title("Pedestrian Animation")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        ax.legend()
    
    ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=100)
    ani.save(output_file, writer="ffmpeg")
    plt.close()
