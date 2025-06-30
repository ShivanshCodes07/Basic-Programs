import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Generate sample data with 3 clusters
np.random.seed(42)
X1 = np.random.normal(0, 1, (100, 2))   # Cluster 1
X2 = np.random.normal(5, 1, (100, 2))   # Cluster 2
X3 = np.random.normal(-5, 1, (100, 2))  # Cluster 3
X = np.vstack([X1, X2, X3])  # Combine all clusters

# Apply Gaussian Mixture Model (GMM)
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X)
labels = gmm.predict(X)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30, alpha=0.6)
plt.scatter(gmm.means_[:, 0], gmm.means_[:, 1], c='red', marker='x', s=100, label="Cluster Centers")
plt.title("Gaussian Mixture Model (GMM) Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
