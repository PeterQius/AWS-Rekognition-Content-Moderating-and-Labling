# AWS Rekognition Content Moderating&Labling(Picture、Video)
AWS Rekognition Content Moderating&Labling(Picture、Video)
# 背景信息
随着业务的增长，在对UGC内容进行标注和审核时，人力的成本和管理将面临非常大的挑战，主要集中在以下几点：  
* 提高审核效率
* 节省审核人力
* 审核流程自动化
* 提取标  

Amazon Rekognition使用深度学习来检测明显或暗示性的成人内容、暴力内容、武器、视觉干扰内容、毒品、酒精、烟草、仇恨符号、赌博，以及图像和视频中的粗鲁手势。除了根据存在的不当或冒犯性内容对图像或视频进行标记之外，Amazon Rekognition还会返回一个带有置信度的分级标签列表。这些标签会指明所检测到的内容类型的特定子类别，从而让开发人员能够进行更精细化的控制，以便筛选和管理大量用户生成的内容(UGC)。这一API可以用于社交和交友网站、相片分享平台、博客和论坛、儿童应用程序、电子商务网站、娱乐和在线广告服务等应用场景。

# 架构流程
#### 架构图
<div align=center><img width="700" alt="image" src="https://user-images.githubusercontent.com/19642366/164969074-80bf5011-653f-4f43-9e41-4104f6e17640.png"></div>

#### 架构特点
*	基于AWS审核的各个接口，可以灵活的选择使用方式，满足不同场景的使用。如上图中，通过直接上传图片或视频，或通过前端业务进行视频抽帧等方式，都可以满足对审核系统的输入，方便用户在成本和效果上实现平衡。
*	AWS各个审核接口相互间不强绑定，可以通过调整其中的某一个置信度（AWS将识别率与置信度结合，来输出是否违规的结果），灵活的进行调整不同场景的识别效果。并且AWS完全开放置信度的配置，供用户实现定制化的需求。
*	AWS的产品和功能与业务架构完全松耦合。如上面架构图中，用户可以有自己的审核、质检等平台或人工复检，并将AWS的结果或分数，结合到一起进行判断，使之更贴近业务和实际场景。

#### 内容审核扩展方案
依托AWS的松耦合特性，方案还能进行多方面扩展，如集成文字（下一章节介绍），机器学习、自研模型等。如下面示例的思路，在置信度识别较低的情况下（场景不同，识别出的效果不同），可以进行切分后再审，实现更高的识别效果。
<div align=center><img width="500" alt="image" src="https://user-images.githubusercontent.com/19642366/164969217-bdc15c80-f1a7-44c4-83a0-f1152660da5d.png"></div>

# 代码部署
1、视频内容抽帧：
<div align=center><img width="500" alt="image" src="https://user-images.githubusercontent.com/19642366/164971103-2df4df65-4f1c-4149-895d-fa0812cd8481.png"></div>

getimage.sh：使用FFmpeg来抽取视频的帧图片，其中fps指明按照多少帧来截取图片。帧率决定了一个视频抽取多少图片，会涉及到调用费用和管理等方面。

2、图片审核：
<div align=center><img width="500" alt="image" src="https://user-images.githubusercontent.com/19642366/164971095-af3ba5eb-0fbd-4743-9f5c-9dfa0f99626c.png"></div>

detectunsafe.py：将图片通过Rekognition进行审核并输出，此处输出到Excel，也可以保存到数据库等。其中Confidence代表标签的置信度，可以通过修改置信度默认值，显示更多标签，建议根据实际情况进行调整。

3、标签提取
detectlabels.py：通过detect_labels接口提取图片包含的标签，同样通过调整置信度，可以控制标签的输出精度。

4、分割图片提升准确度
<div align=center><img width="416" alt="image" src="https://user-images.githubusercontent.com/19642366/164971328-f64d1338-608a-4a8e-b116-2acbb32beb6c.png"></div>

spimg.py：有时候截取的图片中包含的元素过多，同时经过实际测试，Rekognition在审核的时候违规范围也会对结果产生影响。所以在进行了切割之后，能排出干扰，并且放大效果。但同时切割意味着图片会翻倍，所以建议用作复检、抽样等场景。

5、视频审核
视频审核采用了不同的方案和底层模型，识别准确度会更高，价格会相对高一些。此次不对视频审核进行描述，有需要可参考官方文档：https://docs.aws.amazon.com/zh_cn/rekognition/latest/dg/video.html

# 接口测试
Cross_Region_Detectedunsafe.py：跨区域部署调用图片进行接口及延时测试。  
Http_Detectedunsafe.py：调用Http图片进行接口及延时测试。  
Local_Detectedunsafe.py：调用本地图片进行接口及延时测试。
