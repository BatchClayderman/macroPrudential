import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))#解析进入程序所在目录
output = "output.txt"


with open(output, "w", encoding = "utf-8") as fw:
	for filepath in os.listdir():
		if filepath.lower().endswith(".m"):
			try:
				with open(filepath, "r", encoding = "gbk") as fr:
					fw.write("*" * 5 + " " + filepath + " " + "*" * 5 + "\n")
					fw.write(fr.read())
					fw.write("\n" * 2)
			except:
				try:
					with open(filepath, "r", encoding = "utf-8") as fr:
						fw.write("*" * 5 + " " + filepath + " " + "*" * 5 + "\n")
						fw.write(fr.read())
						fw.write("\n" * 2)
				except:
					try:
						with open(filepath, "r", encoding = "utf-16") as fr:
							fw.write("*" * 5 + " " + filepath + " " + "*" * 5 + "\n")
							fw.write(fr.read())
							fw.write("\n" * 2)

					except:
						print("Error:", filepath)