import ifcopenshell
import classes
#import functions



# File path
file = ifcopenshell.open("Clinic.ifc")

# Initialisation for Object Values
i = 0
k = 0
build = []
storey = []
# room = []
# floor_len = {}
# Initialisation for Features Extraction
buildings = file.by_type("IfcBuilding")
floors = file.by_type("IfcBuildingStorey")
relations = file.by_type("IfcRelAggregates")

for building in buildings:
    classes.Building.b_count += 1
    build.append(classes.Building(building.get_info()["GlobalId"], building.get_info()["Name"], building.get_info()["type"]))
    for floor in floors:
        for relation in relations:
            relatingObject = relation.get_info()["RelatingObject"]
            if relatingObject.get_info()["type"] == "IfcBuilding":
                if relatingObject.get_info()["id"] == building.get_info()["id"]:
                    for relatedObject in relation.get_info()["RelatedObjects"]:
                        if relatedObject.get_info()["type"] == "IfcBuildingStorey":
                            classes.Storeys.s_count += 1
                            build[k].storeys.append(classes.Storeys(floor.get_info()["GlobalId"], floor.get_info()["Name"], floor.get_info()["type"]))

            elif relatingObject.get_info()["type"] == "IfcBuildingStorey":
                if relatingObject.get_info()["id"] == floor.get_info()["id"]:
                    for relatedObject in relation.get_info()["RelatedObjects"]:
                        if relatedObject.get_info()["type"] == "IfcSpace":
                            classes.Spaces.sp_count += 1
                            build[k].storeys[i].spaces.append(classes.Spaces(relatedObject.get_info()["GlobalId"], relatedObject.get_info()["Name"], relatedObject.get_info()["type"]))


    # floor_len[i] = k
        i += 1
    k += 1
    print "\n"

def building_assign():
    temp = 0
    for bl in build:
        temp += 1
        print temp
        bl.print_prop()
    temp = 0
    chch = input("Choose the Building you want to assign the properties to : \n")
    for bl in build:
        temp += 1
        if chch == temp:
            A = input("Give Access level to this Building[between 1-3]: \n")
            S = input("Give Security level to this Building[between 1-3]: \n")
            bl.acc = A
            bl.sec = S

            for fl in bl.storeys:
                if fl.acc is None:
                    fl.acc = A
                    for sp in fl.spaces:
                        if sp.acc is None:
                            sp.acc = A
                if fl.sec is None:
                    fl.sec = S
                    for sp in fl.spaces:
                        if sp.sec is None:
                            sp.sec = S

            print "The security properties of this Building has been updated to A", bl.acc, "S", bl.sec


def floor_assign():
    temp = 0
    for bl in build:
        temp += 1
        print temp, bl.name
    temp = 0
    chch = input("Choose the Building of the floor you want to change the properties for :")
    for bl in build:
        temp += 1
        if temp == chch:
            temptem = 0
            for fl in bl.storeys:
                temptem += 1
                print temptem, fl.print_prop()
            temptem = 0
            chchch = input("Choose the floor you want to assign the properties to :")
            for fl in bl.storeys:
                temptem += 1
                if temptem == chchch:
                    As = input("Choose the Access level for this floor [from 1-3] :")
                    Ss = input("Choose the Security level for this floor [from 1-3]")
                    fl.acc = As
                    fl.sec = Ss

                    for sp in fl.spaces:
                        sp.acc = As
                        sp.sec = Ss


def space_assign():
    temp = 0
    for bl in build:
        temp += 1
        print temp, bl.name
    temp = 0
    chch = input("Choose the Building of the space you want to change the properties for :")
    for bl in build:
        temp += 1
        if temp == chch:
            temptem = 0
            for fl in bl.storeys:
                temptem += 1
                print temptem, fl.name
            temptem = 0
            chchch = input("Choose the floor of the space you want to assign the properties to :")
            for fl in bl.storeys:
                temptem += 1
                if temptem == chchch:
                    temptemte = 0
                    for sp in fl.spaces:
                        temptemte += 1
                        print temptemte, sp.print_prop()
                    temptemte = 0
                    chchchc = input("Choose the space you want to assign the properties to :")
                    for sp in fl.spaces:
                        temptemte += 1
                        if temptemte == chchchc:
                            Ass = input("Choose the Access level for this space [from 1-3] :")
                            Sss = input("Choose the Security level for this space [from 1-3] :")
                            sp.acc = Ass
                            sp.sec = Sss



def print_menu():
    print 30 * "-", "MENU", 30 * "-"
    print "1. Show IfcBuildings, IfcStoreys and IfcSpaces \n"
    print "2. Show devices and connections in a building \n"
    print "3. Show assignment \n"
    print "4. Assign properties \n"
    print "Press X to exit \n"
    print 67 * "-"



def print_assign_menu():
    print 30 * "-", "Choose one assignment", 30*"-"
    print "1. Building \n"
    print "2. Floor \n"
    print "3. Space \n"
    print "Press X to go one exit the assignment menu \n"
    print 67 * "-"
    choice = raw_input("Enter your choice :\n")

    if choice == '1':
        print "The building assignment routine starts \n"
        building_assign()

    if choice == '2':
        print "Floor assignment routine starts here \n"
        floor_assign()

    if choice == '3':
        print "Space assignment routine starts here \n"
        space_assign()

loop = True
while loop:
    print_menu()
    choice = raw_input("Enter your choice [1-4] :")

    if choice == '1':
        print "Menu 1"
        print "Total Buildings :", classes.Building.b_count
        print "Total floors :", classes.Storeys.s_count
        print "Total rooms:", classes.Spaces.sp_count
        for bl in build:
            bl.print_prop()
            for fl in bl.storeys:
                fl.print_prop()
                for sp in fl.spaces:
                    print sp.print_prop()
        #functions.show_details() #call the appropriate sequence
    elif choice == '2':
        print "Menu 2"  #call the appropriate sequence

    elif choice == '3':
        print "Menu 3"
        for bl in build:
            print "The assignment for the Building", bl.print_prop(), bl.print_sec_prop()
            for fl in bl.storeys:
                print "The assignment for the floor", fl.print_prop(), fl.print_sec_prop()
                for sp in fl.spaces:
                    print "The assignment for the room", sp.print_prop(), sp.print_sec_prop()

    elif choice == '4':
        print "Menu 4"  #call the appropriate sequence
        print_assign_menu()

    elif choice == 'X' or 'x':
        loop = False

    else:
        raw_input("Wrong option selected, continue and try again by pressing any key")




# for x in storey:
#     print "The name of the floor is ", x.f_name, "with the id : " ,x.f_id, "and access and sec levels", x.f_acc, x.f_sec
#     print "\n"
#     for y in room:
#         if(y.fl_id == x.f_id):
#             print "\t This floor contains", y.sp_name, "with the id : ", y.sp_id, "and access and sec", y.sp_acc, y.sp_sec
#j = 0
# dict_fl = {}
# print "The list of floors in the building is as follows"
# j = 0
# for x in storey:
#     dict_fl[j] = x.f_name
#     j += 1
# print dict_fl
#
# ch = input("Choose the floor on which you want to see the rooms\n")
# for x in dict_fl:
#     if ch == x:
#         if ch > 0:
#             for z in range(floor_len[ch-1], floor_len[ch]):
#                 print room[z].sp_name, "\n", room[z].sp_id, room[z].floor.f_name
#                 print "\n"
#         else:
#             for z in range(0, floor_len[1]):
#                 print room[z].sp_name, "\n", room[z].sp_id, room[z].floor.f_name
#
# print dict_fl
# p = input("Choose the floor number you want to change!!\n")
# for x in storey:
#     if dict_fl[p] == x.f_name:
#         functions.floor_prop_change(x)
#         print x.f_name, "is being changed to", "A", x.f_acc, "S", x.f_sec