#
# # Floor Class Definition
# class Floor:
#     fc = 0  # Floor Count initialiser
#
#     def __init__(self, f_name, f_id, f_acc=None, f_sec=None):
#         self.f_name = f_name
#         self.f_id = f_id
#         self.f_acc = f_acc
#         self.f_sec = f_sec
#         Floor.fc += 1
#
#
# # Space Subclass Definition
# class Space(Floor):
#     sc = 0  # Space Count initialiser
#
#     def __init__(self, sp_name, sp_id, floor, fl_id, sp_acc=None, sp_sec=None):
#         self.sp_name = sp_name
#         self.sp_id = sp_id
#         self.floor = floor
#         self.fl_id = fl_id
#         self.sp_acc = sp_acc
#         self.sp_sec = sp_sec
#         Space.assign_prop(self)
#         Space.sc += 1
#
#     def assign_prop(self):
#         self.fl_id = self.floor.f_id
#         if self.sp_acc is None:
#             self.sp_acc = self.floor.f_acc
#         if self.sp_sec is None:
#             self.sp_sec = self.floor.f_sec
#
#     def change_prop(self, acc=None, sec=None):
#         if acc is not None:
#             self.sp_acc = acc
#         if sec is not None:
#             self.sp_sec = sec
#
#
# # def floor_prop_change(floor):
# #     ac = input("Choose the access level of the floor from 0,1 and 2")
# #     sl = input("Choose the security level of the floor from 0,1 and 2")
# #     main.x.f_acc = ac
# #     main.x.f_sec = sl
# #     print "The floor", main.x.f_acc, "has attributes has been updated", "A", main.x.f_acc, "S", main.x.f_sec


class Concept:

    def __init__(self, acc = None, sec = None, cr_loc = None, cr_remote = None):
        self.acc = acc
        self.sec = sec
        self.cr_loc = cr_loc
        self.cr_remote = cr_remote

    def print_sec_prop(self):
        print "ACC : \tA", self.acc, "\nSEC : \tS", self.sec
        print "\nIndividual Criticality : \tC", self.cr_loc, "Connected Criticality : \tC", self.cr_remote


class IfcProp:

    def __init__(self, guid, name, ifctype):
        self.guid = guid
        self.name = name
        self.type = ifctype

    def print_prop(self):
        print "GUID :", self.guid, "NAME :", self.name, "TYPE :", self.type


class Site(Concept, IfcProp):
    # b_count = 0

    def __init__(self, guid, name, ifctype, buildings, acc = None, sec = None, cr_loc = None):
        self.buildings = []
        IfcProp.__init__(self, guid, name, ifctype)
        Concept.__init__(self, acc, sec, cr_loc)

class Building(Concept, IfcProp):
    b_count = 0

    def __init__(self, guid, name, ifctype, storeys=None, acc = None, sec = None, cr_loc = None):
        self.storeys = []
        IfcProp.__init__(self, guid, name, ifctype)
        Concept.__init__(self, acc, sec, cr_loc)

class Storeys(Concept, IfcProp):
    s_count = 0

    def __init__(self, guid, name, ifctype, spaces=None, acc=None, sec=None, cr_loc=None):
        self.spaces = []
        IfcProp.__init__(self, guid, name, ifctype)
        Concept.__init__(self, acc, sec, cr_loc)

class Spaces(Concept, IfcProp):
    sp_count = 0

    def __init__(self, sp_guid, sp_name, sp_ifctype, devices=None, acc=None, sec=None, cr_loc=None):
        self.devices = []
        IfcProp.__init__(self, sp_guid, sp_name, sp_ifctype)
        Concept.__init__(self, acc, sec, cr_loc)