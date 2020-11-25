from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

# 构建模型框架，指定变量之间的依赖关系
student_model = BayesianModel([('D', 'G'),
                               ('I', 'G'),
                               ('I', 'S'),
                               ('G', 'L')])

# 构建各个节点和传入概率表并指定相关参数
grade_cpd = TabularCPD(
    variable='G',   # 节点名称
    variable_card=3,    # 节点取值个数
    values=[[0.3, 0.05, 0.9, 0.5],  # 该节点概率表
            [0.4, 0.25, 0.08, 0.3],
            [0.3, 0.7, 0.02, 0.2]],
    evidence=['I', 'D'],    # 依赖节点
    evidence_card=[2, 2]    #依赖节点的取值个数
)
difficulty_cpd = TabularCPD(
    variable='D',
    variable_card=2,
    values=[[0.6], [0.4]]
)
intel_cpd = TabularCPD(
    variable='I',
    variable_card=2,
    values=[[0.7], [0.3]]
)
letter_cpd = TabularCPD(
    variable='L',
    variable_card=2,
    values=[[0.1, 0.4, 0.99],
            [0.9, 0.6, 0.01]],
    evidence=['G'],
    evidence_card=[3]
)
sat_cpd = TabularCPD(
    variable='S',
    variable_card=2,
    values=[[0.95, 0.2],
            [0.05, 0.8]],
    evidence=['I'],
    evidence_card=[2]
)

# 将包含概率表的各节点添加到模型中
student_model.add_cpds(
    grade_cpd,
    difficulty_cpd,
    intel_cpd,
    letter_cpd,
    sat_cpd
)

# 获取模型的条件概率分布
student_model.get_cpds()

# 获取各节点间的依赖关系
student_model.get_independencies()

# 进行贝叶斯推断
student_infer = VariableElimination(student_model)
prob_G = student_infer.query(
    variables=['G'],
    evidence={'I':1,'D':0})
print(prob_G)