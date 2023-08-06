# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coco_loader']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.4,<0.6.0']

setup_kwargs = {
    'name': 'coco-loader',
    'version': '0.0.1',
    'description': 'COCO dataset loader.',
    'long_description': "# coco-loader\n\nCOCO dataset loader.\nProvides serializable native Python bindings for several COCO dataset formats.\n\nSupported bindings and their corresponding modules:\n\n- Object Detection: `objectdetection`\n- Keypoint Detection: `keypointdetection`\n- Panoptic Segmentation: `panopticsegmentation`\n- Image Captioning: `imagecaptioning`\n\n## Installation\n\n`coco-loader` is available on PyPI:\n\n```bash\npip install coco-loader\n```\n\n## Usage\n\n### Creating a dataset (Object Detection)\n\n```python\n>>> from coco_loader.common import Info, Image, License\n>>> from coco_loader.objectdetection import ObjectDetectionAnnotation, \\\n...                                      ObjectDetectionCategory, \\\n...                                      ObjectDetectionDataset\n>>> from datetime import datetime\n>>> info = Info(  # Describe the dataset\n...    year=datetime.now().year,\n...    version='1.0',\n...    description='This is a test dataset',\n...    contributor='Test',\n...    url='https://test',\n...    date_created=datetime.now()\n... )\n>>> mit_license = License(  # Set the license\n...     id=0,\n...     name='MIT',\n...     url='https://opensource.org/licenses/MIT'\n... )\n>>> images = [  # Describe the images\n...     Image(\n...         id=0,\n...         width=640, height=480,\n...         file_name='test.jpg',\n...         license=mit_license.id,\n...         flickr_url='',\n...         coco_url='',\n...         date_captured=datetime.now()\n...     ),\n...     ...\n... ]\n>>> categories = [  # Describe the categories\n...     ObjectDetectionCategory(\n...         id=0,\n...         name='pedestrian',\n...         supercategory=''\n...     ),\n...     ...\n... ]\n>>> annotations = [  # Describe the annotations\n...     ObjectDetectionAnnotation(\n...         id=0,\n...         image_id=0,\n...         category_id=0,\n...         segmentation=[],\n...         area=800.0,\n...         bbox=[300.0, 100.0, 20.0, 40.0],\n...         is_crowd=0\n...     ),\n...     ...\n... ]\n>>> dataset = ObjectDetectionDataset(  # Create the dataset\n...     info=info,\n...     images=images,\n...     licenses=[mit_license],\n...     categories=categories,\n...     annotations=annotations\n... )\n>>> dataset.save('test_dataset.json', indent=2)  # Save the dataset\n```\n\n### Loading a dataset\n\n```python\n>>> from coco_loader.objectdetection import ObjectDetectionDataset\n>>> dataset = ObjectDetectionDataset.load('test_dataset.json')  # Load the dataset\n```\n",
    'author': 'Jinhyuck Cha',
    'author_email': 'jhcha@superb-ai.com',
    'maintainer': 'Jinhyuck Cha',
    'maintainer_email': 'jhcha@superb-ai.com',
    'url': 'https://github.com/jinhyuckcha/coco-loader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
