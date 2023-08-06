

from .dgraph_gateway import dgraph_query
import json


class check_item_type:
    def __init__(self):
        c = dgraph_query()
        self.client = c.get_client()

    def get(self, uid):
        query = """
            { item(func: uid("""+uid+""")) {
                uid
                dgraph.type     
                }
            }"""

        res = self.client.txn(read_only=True).query(query)
        item = json.loads(res.json)
        return item

class get_category_id:
    def __init__(self):
        c = dgraph_query()
        self.client = c.get_client()

    def get(self, uid):
        query = """
            { item(func: uid("""+uid+""")) {
                uid
                dgraph.type 
                categories : Product.product_type {
                    category_id : uid
                    category_code:Category.category_code
                    category_label:Category.category_label
                    parent:~Category.category_children {
                        category_id:uid
                        category_code:Category.category_code
                        category_label:Category.category_label
                            
                        }

                    }

                }
            }"""

        res = self.client.txn(read_only=True).query(query)
        item = json.loads(res.json)
        return item["item"][0]["categories"]["parent"][0]["category_id"]


class dqaddress(address):
    query = dgraph_query()


class dqcart(dqvirtualcart):
    query = dgraph_query()


class dqnewcart(cart):
    query = dgraph_query()


class dqwishlist(wishlist):
    query = dgraph_query()

class dqwishlist_check(wishlist_check):
    query = dgraph_query()

class dqcode_generator(code_generator):
    query = dgraph_query()


class dqcatcode(catcode_generator):
    query = dgraph_query()


class dgraph_inventory(inventory):
    query = dgraph_query()


class dqcategory(category):
    query = dgraph_query()


class dqproduct(product):
    query = dgraph_query()


class dqgrade(grade):
    query = dgraph_query()


class dqbrand(brand):
    query = dgraph_query()


class dqspecification(specification):
    query = dgraph_query()


class dqpolicy(policy):
    query = dgraph_query()


class dqdelivery(delivery):
    query = dgraph_query()


class dqtax(tax):
    query = dgraph_query()


class dqcess(cess):
    query = dgraph_query()


class dqstatecess(statecess):
    query = dgraph_query()


class dqproducttax(producttax):
    query = dgraph_query()


class dqfulfillment(fulfillment):
    query = dgraph_query()


class dqhyperclass_services(hyperclass_services):
    query = dgraph_query()


class dqservices(services):
    query = dgraph_query()


class dqtasks(tasks):
    query = dgraph_query()


class dqlocation(location):
    query = dgraph_query()


class dqcountry(country):
    query = dgraph_query()


class dqstate(state):
    query = dgraph_query()
