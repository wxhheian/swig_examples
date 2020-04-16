from distutils.core import setup,Extension

#生成一个拓展模块
pht_module = Extension('_EncryptTool',  #swig模块引用的模块名称，必须要有下划线
                sources=['EncryptTool_wrap.cxx',   #封装后的接口文件
                        'EncryptTool.cpp',    #原始代码所依赖的文件
                        ],
                        )

setup(name = 'EncryptTool',   #打包后的名字，也是外面python导包的名字
        version = '0.1',      #版本号
        author = 'WXHhh',     #封装作者
        description = 'simple swig pht from docs',  #描述信息
        ext_modules = [pht_module],    #与上面的拓展模块名称一致
        py_modules = ['EncryptTool'],    #需要打包的模块列表
        )
