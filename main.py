import os

jdk_dir = {
    'java8': 'D:\\Program Files\\Java\\jdk1.8.0_333',
    'java18': 'D:\\Program Files\\Java\\jdk18.0.2'
}

if __name__ == '__main__':
    # 输出jdk_dir
    print("JDK version-list:")
    for k in jdk_dir:
        print(k + ' - ' + jdk_dir[k])

    jdk_version = input("\nPlease choose one JDK version\n")

    if jdk_version in jdk_dir.keys():
        switched_jdk_dir = jdk_dir[jdk_version]

        # 判断末尾是否存在 \
        if switched_jdk_dir.endswith("\\"):
            switched_jdk_dir = switched_jdk_dir[:-1]
        command = "setx \"JAVA_HOME\" \"" + switched_jdk_dir + "\" /m"
        # 设置 JAVA_HOME 环境变量
        os.system(command)
        print("JAVA_HOME has changed to " + switched_jdk_dir)

        # 判断是否存在 JRE_HOME 环境变量
        if os.environ.get("JRE_HOME") is not None:
            jre_dir = switched_jdk_dir + "\\jre"
            # 判断 JRE 路径是否存在
            if os.path.exists(jre_dir):
                command = "setx \"JRE_HOME\" \"" + switched_jdk_dir + "\\jre\" /m"
                os.system(command)
                print("JRE_HOME has changed to " + jre_dir)
    else:
        print("invalid JDK version")