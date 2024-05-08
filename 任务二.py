from some_nerc_library import NamedEntityRecognizer
from some_graph_library import Graph
from some_event_extraction_library import EventExtractor

# 假设已经有了《三国演义》的文本数据
text = get_text("三国演义.txt")

# 文本预处理
preprocessed_text = preprocess(text)

# 使用NER识别人物
ner = NamedEntityRecognizer()
entities = ner识别(preprocessed_text)

# 构建图谱
graph = Graph()
for entity in entities:
    if entity == "诸葛亮":
        graph.add_node(entity)
    else:
        # 确定人物之间的关系
        relationship = determine_relationship(entity, "诸葛亮")
        if relationship:
            graph.add_edge(entity, "诸葛亮", relationship)

# 事件提取
event_extractor = EventExtractor()
events = event_extractor.extract_events(preprocessed_text, "诸葛亮")

# 事件大纲生成和优先级模型建立
event_outline = generate_event_outline(events)
priority_model = build_priority_model(events)

# 排序
sorted_events = sort_events(priority_model)

# 系统泛化
def analyze_character(character, chapter):
    # 针对不同的人物和篇章重复上述步骤
    pass

# 关键字提取
keywords =input("输入你想查阅的人物(所有称呼都必须包括):[]") 

# 搜索关键词，提取相关句子
relevant_sentences = []
for sentence in sentences:
    # 使用任意关键词匹配句子，如果匹配成功，则添加到结果列表
    if any(keyword in sentence for keyword in keywords):
        relevant_sentences.append(sentence)

# 结果展示
visualize(graph, sorted_events)

# 运行系统
analyze_character("[]")
