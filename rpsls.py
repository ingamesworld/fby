#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��벩Ԩ
���ڣ�2021.12.1
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��
    if name=="ʯͷ":
        name=0
    elif name=="ʷ����":
        name=1
    elif name=="��":
        name=2
    elif name=="����":
        name=3
    elif name=="����":
        name=4
    else: name="Error: No Correct Name"
    return name

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��
    if number==0:
        number="ʯͷ"
    if number==1:
        number="ʷ����"
    if number==2:
        number="��"
    if number==3:
        number="����"
    if number==4:
        number="����"
    return number

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    if player_choice==0:
        if answer==3:
            print("��Ӯ��")
        elif answer==4:
            print("��Ӯ��")
        elif answer==1:
            print("����Ӯ��")
        elif answer==2:
            print("����Ӯ��")
        else:print("���ͼ��������һ����")
    elif player_choice==1:
        if answer==0:
            print("��Ӯ��")
        elif answer==4:
            print("��Ӯ��")
        elif answer==2:
            print("����Ӯ��")
        elif answer==3:
            print("����Ӯ��")
        else:print("���ͼ��������һ����")
    elif player_choice==2:
        if answer==1:
            print("��Ӯ��")
        elif answer==0:
            print("��Ӯ��")
        elif answer==3:
            print("����Ӯ��")
        elif answer==4:
            print("����Ӯ��")
        else:print("���ͼ��������һ����")
    elif player_choice==3:
        if answer==1:
            print("��Ӯ��")
        elif answer==2:
            print("��Ӯ��")
        elif answer==0:
            print("����Ӯ��")
        elif answer==4:
            print("����Ӯ��")
        else:print("���ͼ��������һ����")
    elif player_choice==4:
        if answer==3:
            print("��Ӯ��")
        elif answer==2:
            print("��Ӯ��")
        elif answer==1:
            print("����Ӯ��")
        elif answer==0:
            print("����Ӯ��")
        else:print("���ͼ��������һ����")
    else:player_choice="Error: No Correct Name"

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass
print("��ӭʹ��RPSLS��Ϸ")
player_choice=input("����������ѡ��:")
print("----------------")
answer=random.randint(0,4)
player_choice_number=name_to_number(player_choice)
computer_number=number_to_name(answer)
if player_choice_number=="Error: No Correct Name":
    print(player_choice_number)
else:
    print("����ѡ��Ϊ��%s"%player_choice)
    print("�������ѡ��Ϊ��%s"%computer_number)
    rpsls(player_choice_number)


