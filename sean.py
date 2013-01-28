import freshbooks
# get data
freshbooks.setup('sumosoftware.freshbooks.com','4668d90e024786abce6feed39e7de0fa') 
clients = freshbooks.Client.list()
client_1 = freshbooks.Client.get(0)

# update data
# changed_client = freshbooks.Client()
# changed_client.client_id = client_1.client_id
# changed_client.first_name = u'Jane'
# r = freshbooks.call_api('client.update', changed_client)
# assert(r.success)