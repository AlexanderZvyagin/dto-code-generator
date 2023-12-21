import logging

log = logging.getLogger(__name__)

class Mapping:
    pass

class Version:
    def __init__ (self,name:str,id:int):
        self.name = name
        self.id   = id
    def __eq__ (self,other):
        return self.name == other.name and self.id == other.id

class Converter:
    def __init__ (self,name:str,id_from:int,id_to:int,function):
        self.name = name
        self.id_from = id_from
        self.id_to   = id_to
        self.function = function
    def __repr__ (self):
        return f'Converter[{self.name} {self.id_from}=>{self.id_to}]'

class B1:
    def __init__ (self,x:int=0):
        self.version = Version('B',1)
        self.x = x

class B2:
    def __init__ (self,x:int=0,y:int=0):
        self.version = Version('B',2)
        self.x = x
        self.y = y

class B3:
    def __init__ (self,x:int=0,y:int=0,name:str=''):
        self.version = Version('B',3)
        self.x = x
        self.y = y
        self.name = name

class B4:
    def __init__ (self,x:int=0,y:int=0,tags=[]):
        self.version = Version('B',4)
        self.x = x
        self.y = y
        self.tags = tags

def convert_B1_to_B2(b1:B1) -> B2:
    return B2(b1.x,0)

def convert_B1_to_B3(b1:B1) -> B3:
    return B3(b1.x,0,'')

def convert_B2_to_B3(b2:B2) -> B3:
    return B3(b2.x,b2.y,'')

def convert_B2_to_B4(b2:B2) -> B4:
    return B4(b2.x,b2.y)

def convert_B3_to_B4(b3:B3) -> B4:
    return B4(b3.x,b3.y,[] if b3.name=='' else [b3.name])

class Mapping:
    def __init__ (self):
        self.converters = []

    def FindConverter (self,name,version_from,version_to,candidates_chain=[]):

        log.debug(f'FindConverter {name} {version_from} {version_to} {candidates_chain}')

        if version_from==version_to:
            return []

        candidates = []
        for c in self.converters:
            if name != c.name:
                continue
            if version_from != c.id_from:
                continue
            log.debug(f'Adding a candidate: {c}')
            candidates.append(c)
            if version_to != c.id_to:
                continue
            log.debug(f'Found a final converter: {c}')
            return candidates_chain+[c]

        log.debug(f'Not found, but there are {len(candidates)} candidates.')

        chains_list = []
        for candidate in candidates:
            chain_copy = [x for x in candidates_chain]
            chain_copy.append(candidate)
            v = self.FindConverter(name,candidate.id_to,version_to,chain_copy)
            if v is None:
                continue
            log.debug(f'Found a cain of length {len(v)}')
            chains_list.append(v)

        log.debug(f'len(chains_list)={len(chains_list)} ')

        if len(chains_list)==0:
            return None

        def shortest_chain(chains):
            x = chains[0]
            for c in chains[1:]:
                if len(c)<len(x):
                    x = c
            return x

        return shortest_chain(chains_list)

    def Convert (self, obj, version_to:int):

        converters_chain = self.FindConverter(obj.version.name,obj.version.id,version_to)
        log.debug(f'{converters_chain}')
        if converters_chain is not None:
            log.debug(f'converters_chain length is {len(converters_chain)}')
            for convert in converters_chain:
                obj = convert.function(obj)
        
        return obj

def test_B1_to_B4_conversion_with_mapping():

    m = Mapping()
    m.converters.append(Converter ('B',1,2,convert_B1_to_B2))
    m.converters.append(Converter ('B',1,3,convert_B1_to_B3))
    m.converters.append(Converter ('B',2,3,convert_B2_to_B3))
    m.converters.append(Converter ('B',3,4,convert_B3_to_B4))

    b1 = B1(111)

    b4 = m.Convert(b1,4)

    assert b1.version == Version('B',1)
    assert b4.version == Version('B',4)
    assert b4.x == b1.x
    assert b4.y == 0
    assert b4.tags == []

def test_B1_to_B1_conversion_with_mapping():

    m = Mapping()
    m.converters.append(Converter ('B',1,2,convert_B1_to_B2))
    m.converters.append(Converter ('B',1,3,convert_B1_to_B3))
    m.converters.append(Converter ('B',2,3,convert_B2_to_B3))
    m.converters.append(Converter ('B',3,4,convert_B3_to_B4))

    b1 = B1(111)

    b1_ = m.Convert(b1,1)

    assert id(b1) == id(b1_)