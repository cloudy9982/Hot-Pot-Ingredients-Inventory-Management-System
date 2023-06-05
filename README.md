# 關東煮存貨管系統 backend

# 安裝方法 
``` pip install -r requirements.txt ```

# 使用操作
`python db.py`，fake deta出現在instance資料夾內
`python app.py`，開啟主程式

![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/程式執行.png)


frontend connected backend
clone front 後，下載完能正常開啟，操作以下指令

> backend
`python db.py`
`python app.py`

> frontend
`npm install`
`npm run build`
`npm start `

# 檢查語法
`pylint <檔案名稱.py>`

# 檢查unit test
`python -m unittest discover`

# 前端畫面
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/前端呈現畫面.png)


訂單主畫面
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/order.png)


訂單詳細各別內容
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/order_detail.png)


新增tag
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/add_tag.png)


新增item
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/add_item.png)


item詳細內容
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/item_detail.png)


刪除item
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/delete_item.png)


更新item
![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/update_item.png)


# gitlab_CICD

![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/gitlabCICD.png)



![Image text](https://github.com/cloudy9982/Hot-Pot-Ingredients-Inventory-Management-System/blob/master/img-folde/gitlabCICD_detail.png)

install-dependencies：下載requirements.txt套件環境

unit-test-job：測試unittest（item,tag,order CRUD）

lint-test-job：使用pylint找出潛在錯誤、程式錯誤、程式碼風格問題 => 提高程式碼的品質和可維護性

coverage-job：計算代碼的覆蓋率。它可以跟踪測試用例執行期間經過的代碼行，並生成相應的報告，指示哪些代碼已經執行，哪些代碼沒有執行。

pre-deploy：生成fake data
