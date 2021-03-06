def pdb_writer(protein, model_number, output):
    num_atom= 1
    num_res= 1
    with open(output,'a+') as f: 
        f.write("MODEL".ljust(6) + "    " + str(model_number).rjust(4))
    for res in protein :
          with open(output,'a+') as f:            
             f.write("\n")
             f.write("ATOM".ljust(4))
             f.write("  ")
             f.write(str(num_atom).rjust(5))
             f.write("  ")
             f.write("CA".ljust(3))
             f.write(" ")
             if res.polarity == "H":
                 f.write("LEU".ljust(3))
             elif res.polarity == "P":
                 f.write("CYS".ljust(3))
             f.write(" ")
             f.write("A")
             f.write(str(num_res).rjust(4))
             f.write("    ")
             coo1_ang=res.coordinates[0]*3.4
             coo1_r=format(coo1_ang, '.3f')
             f.write(str(coo1_r).rjust(8))
             coo2_ang=res.coordinates[1]*3.4
             coo2_r=format(coo2_ang, '.3f')
             f.write(str(coo2_r).rjust(8))
             #f.write("\n")  
             num_atom= num_atom+1
             num_res=num_res+1
    with open(output,'a+') as f:
        f.write("\n")
        f.write("TER")
        f.write("\n")
        f.write("ENDMDL")
        f.write("\n")  
