from project_Doc_M_CSM.category import Category
from project_Doc_M_CSM.document import Document
from project_Doc_M_CSM.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = [d for d in self.documents if d.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove([c for c in self.categories if c.id == category_id][0])

    def delete_topic(self, topic_id):
        self.topics.remove([t for t in self.topics if t.id == topic_id][0])

    def delete_document(self, document_id):
        self.documents.remove([d for d in self.documents if d.id == document_id][0])

    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):
        return "\n".join([repr(x) for x in self.documents])
