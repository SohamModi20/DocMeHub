from reader import Reader
import cv2
import numpy as np
if __name__=="__main__":
    reader=Reader()
    pdf_path="E:\\Downloads\\SalesInvoice.pdf"
    img_path="E:\\Downloads\\temp.jpg"
    temp_path="E:\\Downloads\\temp2.jpg"
    img=cv2.imread(temp_path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output=reader.read("")
    output.print()