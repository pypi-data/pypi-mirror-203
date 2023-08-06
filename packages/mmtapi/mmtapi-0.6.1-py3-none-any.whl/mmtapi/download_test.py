#import mmtapi
import requests,os, json, datetime


class local_target_file():
     def __init__(self):
          self.filename =  os.path.join(os.getcwd(), 'mmtapi_targets.json')
          if os.path.exists(self.filename):
               of = open(self.filename, 'r')
               self.file = json.load(of)
          else:
               self.file = {
                    'targets':[]
               }
          self.targets = self.file['targets']

     def _save(self):
          self.file['targets'] = self.targets
          fi = open(self.filename, 'w')
          fi.write(json.dumps(self.file))
          fi.close()

     def _get(self, targetid=None):
          assert targetid is not None
          t = [x for x in self.targets if x['_id'] == targetid]
          t = t[0] if len(t) else None
          return t

     def _insert(self, target=None):
          assert target is not None
          if target['_id'] not in [x['_id'] for x in self.targets]:
               self.targets.append(target)
          else:
               self.targets[target['_id']] = target['local_information']

          self._save()
     
     def _delete(self, targetid=None):
          assert targetid is not None
          raise NotImplementedError

if __name__ == '__main__':
     target_file = local_target_file()
     payload = {
          '_id':0,
          'local_information': {
               'partial_download':False,
               'downloaded':True,
               'local_save':False
          }
     }
     target_file._insert(target=payload)



