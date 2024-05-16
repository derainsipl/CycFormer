# CycFormer: Unsupervised Rain Removal Network Based on CycleGAN and Transformer
Jiafeng Li, Xiaoyu Liu, Li Zhuo, Jing Zhang


### Abstract
The single-image rain removal task image deraining task has always been challenging in image processing, and unsupervised rain removal has attracted increasing attention because it can process real rain images without pairwise data. At present, most unsupervised rain removal methods are based on the CycleGAN framework; however, the combination of this framework and the Transformer is not satisfactory owing to the insufficient ability of the Transformer to model real rain features with global inhomogeneous distributions, which prevents it from being fully applicable to unsupervised tasks. In this study, an unsupervised rain removal network based on CycleGAN and the Transformer (CycFormer) is proposed. First, a deformable sparse Transformer structure is developed to obtain global inhomogeneous rain pattern feature information using the attention mechanism. Subsequently, the fusion mechanism for multiscale information in the feedforward network is redesigned to improve the feature modeling capability of small  rain patterns. Finally, the image rain removal task is considered a decomposition task, and a rain layer unsupervised training method for joint positional contrastive learning is proposed to effectively separate the rain patterns. We conducted several experiments on different real and synthetic rain datasets, and the results showed that our method achieved good performance in the unsupervised rain removal task.
![image](./model.png)
![image](./transformer.png)

### Contributions
1) In order to make the network extract rich global features of raindrops, this study designs the Transformer Attention Layer Feature Fusion Module on the network structure, which is the first time that the raindrop features extracted from multiple Transformer Attention Layers are fused for the first time in the de-raindrop task, so as to make the network more adaptable to the globally complex raindrop features.
2) In order to make UNet with global-local modeling capability, this study proposes for the first time a transition module between the up- and down-sampling operations, which is obtained by feature fusion of global and local information extractors, and which performs global-local modeling of feature information extracted from the down-sampling operations to help the network perform reconstruction tasks to enhance the detail recovery capability to mitigate artifacts.
3) In order to make the Transformer have the ability of adaptive processing of raindrops, different from the previous Transformer, this study improves the attention mechanism and the feedforward network from the global and local perspectives, respectively. Firstly, the uncertainty-based sparse attention mechanism is proposed to make the network model the global space more efficiently, and further localization is introduced in the three-channel feature information modeling on the feed-forward network for the characteristics of the raindrop image. The Transformer has an extremely comprehensive raindrop feature modeling capability, which can be well adapted to UNet to improve the rain removal performance.

### Video de-rain demo
Click on the “derain.mp4” file on the homepage or click https://github.com/derainsipl/CycFormer/blob/main/derain.mp4.

### Code
The code for this program will be published soon.
