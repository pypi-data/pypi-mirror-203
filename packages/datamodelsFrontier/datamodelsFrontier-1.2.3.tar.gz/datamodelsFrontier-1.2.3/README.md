# Data Models

### Description
This package contains three pydantic data models
Datamodels for use in the API tier and Processing tier

### How to Install
This package is a simple package with three pydantic data models. 
The module is called datamodels.

**Example imports:**

*Command Line*
```bash
$ pip install datamodelsFrontier
```
*Python*
```python
from datamodels.external import Barcode

from datamodels.downstream import ChildProduct
```


### Code Information
#### Example Code:
```python
InventoryItemDimension(height_mm=3, width_mm=4, depth_mm=5, mass_kg=5)
```
#### Each Model and Input Value
##### External
The models that can be imported are:

- InventoryItemDimension:
   - height_mm: int
   - width_mm: int
   - depth_mm: int
   - mass_kg: int


- Barcode:
  - barcode_type: str
  - barcode: str


- InventoryItem:
  - inventory_item_id: str
  - sku: str
  - name: str
  - country_of_origin: str
  - harmonized_system_code: str
  - has_hazmat: bool
  - barcodes: list[Barcode]
  - dimensions: InventoryItemDimension
  - alternative_inventory_items: list[str]
  - thg_id: str 
  - status: str

##### Downstream

- ChildProduct:
  - id: str
  - title: str
  - barcode: str
  - releaseDate: str
  - rrp: str
  - length: str
  - height: str
  - width: str
  - weight: str
  - releaseDateEstimated: bool
