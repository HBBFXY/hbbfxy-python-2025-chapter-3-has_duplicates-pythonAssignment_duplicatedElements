# 这是评分文件，不要修改
import sys
import io
import contextlib
import re

def load_student_function():
    """更健壮的学生函数加载方式"""
    try:
        from main import has_duplicates
        return has_duplicates
    except ImportError:
        print("❌ Error:
        print("❌ 错误: 找不到main.py文件")
    except AttributeError:
        print("❌ 错误: main.py中没有定义has_duplicates函数")
    except SyntaxError as e:
        print(f"❌ 语法错误: {e}")
    except Exception as e:
        print(f"❌ 加载学生模块时出错: {e}")
    return None

def run_main_program():
    """运行学生的主程序并捕获输出"""
    try:
        # 直接执行学生的主程序
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            import main
            return buf.getvalue(), None
    except Exception as e:
        return None, f"运行主程序时出错: {e}"

def test_has_duplicates():
    """测试has_duplicates函数"""
    has_duplicates = load_student_function()
    if has_duplicates is None:
        return False
    
    test_cases = [
        ([], False),
        ([1], False),
        ([1, 2, 3], False),
        ([1, 1], True),
        (["a", "a"], True),
        ([1.a"], True),
        ([1.0, 1.0], True),
        ([True, True], True),
        ([None, None], True),
        ([1, 2, 3, 1], True, 3, 1], True),
        (["a", "b", "a"], True),
        ([[1], [1]], False),
        ([1, 1.0], False),
    ]
    
    passed = 0
    total = len(test_cases)
    
    for test_input, expected in test_cases:
        try:
            result = has_duplicates(test_input)
            if result == expected:
                passed += 1
                print(f"✅ 通过: {test_input} -> {expected}")
            else:
                print {expected}")
            else:
                print(f"❌ 失败: {test_input}")
                print(f"   预期: {expected}, 实际: {result}")
        except Exception as e:
            print(f"❌ 异常: {test_input}")
            print(f"   错误: {e}")
    
    print(f"\n函数测试: {passed}/{total} 通过")
    return passed == total

def test_main_program_output():
    """测试主程序输出"""
    output, error = run_main_program()
    if error:
        print(f"❌ 主程序错误: {error}")
        return False
    if not output:
        print("❌ 主程序没有输出")
        return False
    
    print("\n学生主程序输出:")
    print("-" * 40)
    print(output" * 40)
    print(output)
    print("-" * 40)
    
    # 检查关键输出
    required_outputs = [
        "没有重复元素",
        "有重复元素"
    ]
    
    found = [phrase for phrase in required_outputs if phrase in output]
    
    if len(found) == len(required_outputs):
        print("✅ 主程序输出包含必要内容")
        return True
    
    print("❌ 主程序输出缺少必要内容")
    print(f"需要包含: {', '.join(required_outputs)}")
    return False

if __name__ == "__main__":
    print("=" * 50    print("=" * 50)
    print("开始测试重复元素判定作业")
    print("=" * 50)
    
    func_pass = test_has_duplicates()
    print("\n" +plicates()
    print("\n" + "=" * 50)
    main_pass = test_main_program_output()
    
    if func_pass and main_pass    
    if func_pass and main_pass:
        print("\n🎉 所有测试通过!")
        sys.exit(0)
    else:
        print("\n💥 测试未全部通过")
        sys.exit(1)
通过")
        sys.exit(1)
