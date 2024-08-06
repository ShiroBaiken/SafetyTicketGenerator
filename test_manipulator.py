from pymongo import MongoClient, DESCENDING, ReturnDocument


class MongoCollectionExtention:
    def __init__(self, cli, collection):
        self.db = cli.questions_generator
        self.collection = collection


class QestionGetter(MongoCollectionExtention):

    def __init__(self, cli, collection):
        super().__init__(cli, collection)

    def retrieve_one(self, ind):
        return self.db[self.collection].find_one({"question_id": ind}, {'_id': 0})

    def get_range(self):
        return self.db[self.collection].estimated_document_count()

    def retrieve_all(self):
        return list(self.db[self.collection].find({}, {'_id': 0}))


class QuestionInserter(MongoCollectionExtention):

    def __init__(self, cli: MongoClient, collection: str):
        super().__init__(cli, collection)
        self.template = {'question': '',
                         'question_id': 0}

    def get_next_sequence_value(self, sequence_name):
        sequence_doc = self.db.sequences.find_one_and_update(
            {"_id": sequence_name},
            {"$inc": {"sequence_value": 1}},
            sort=[("_id", DESCENDING)],
            return_document=ReturnDocument.AFTER,
        )
        return sequence_doc["sequence_value"]

    def add_new_question(self, new_question):
        next_question_id = self.get_next_sequence_value("question_id")
        new_entry = {
            "question": new_question,
            "question_id": next_question_id,
        }

        self.db[self.collection].insert_one(new_entry)

    def update_existing_question(self, ind, new_value):
        self.db[self.collection].update_one({"question_id": ind}, {"$set": {"question": new_value}})


class ListsGetter(MongoCollectionExtention):
    def __init__(self, cli: MongoClient, collection: str = 'positions'):
        super().__init__(cli, collection)

    def get_positions(self):
        return self.db[self.collection].find_one({}, {'_id': 0}).values()

    def get_keys(self):
        return self.db[self.collection].find_one({}, {'_id': 0}).keys()


class CollectionGetter(MongoCollectionExtention):
    def __init__(self, cli: MongoClient, collection: str = 'categorises'):
        super().__init__(cli, collection)

    def get_collection(self, key):
        return self.db[self.collection].find_one()[key]


class PositionsManipulator(MongoCollectionExtention):
    def __init__(self, cli: MongoClient, collection: str = "positions"):
        super().__init__(cli, collection)

    def add_new_position(self, new_position):
        current_ind = len(self.db[self.collection].find_one({}, {'_id': 0}).values())
        self.db[self.collection].update_one({}, {"$set": {f"{current_ind + 1}": new_position}})
        return current_ind + 1

    def delete_one(self, position_to_remove):
        positions = self.db[self.collection].find_one({}, {"_id": 0})
        new_positions = list(x for x in positions.values() if x != position_to_remove)
        r = [str(x) for x in range(1, len(new_positions) + 1)]
        to_insert = dict(zip(r, new_positions))
        self.db[self.collection].update_one({}, {"$set": to_insert, "$unset": {f"{len(new_positions) + 1}": 1}})


