import sys
import subprocess
import shlex
import shutil
import argparse
import json
import os
import shutil
import errno
from pprint import pprint

data_table_name = "ariba_databases"

mlst_dict = {
    "achs"	: "Achromobacter spp.",
    "acib1"	: "Acinetobacter baumannii#1",
    "acib2"	: "Acinetobacter baumannii#2",
    "aers"	: "Aeromonas spp.",
    "anap"	: "Anaplasma phagocytophilum",
    "arcs"	: "Arcobacter spp.",
    "aspf"	: "Aspergillus fumigatus",
    "bacc"	: "Bacillus cereus",
    "bacl"	: "Bacillus licheniformis",
    "bacs"	: "Bacillus subtilis",
    "barb"	: "Bartonella bacilliformis",
    "barh"	: "Bartonella henselae",
    "bors"	: "Bordetella spp.",
    "borr"	: "Borrelia spp.",
    "brah"	: "Brachyspira hampsonii",
    "brach"	: "Brachyspira hyodysenteriae",
    "brai"	: "Brachyspira intermedia",
    "brap"	: "Brachyspira pilosicoli",
    "bras"	: "Brachyspira spp.",
    "brus"	: "Brucella spp.",
    "bucc"	: "Burkholderia cepacia complex",
    "burp"	: "Burkholderia pseudomallei",
    "camc"	: "Campylobacter concisus/curvus",
    "camf"	: "Campylobacter fetus",
    "camh"	: "Campylobacter helveticus",
    "rlis"	: "Campylobacter hyointestinalis",
    "cami"	: "Campylobacter insulaenigrae",
    "camj"	: "Campylobacter jejuni",
    "caml"	: "Campylobacter lanienae",
    "rari"	: "Campylobacter lari",
    "cams"	: "Campylobacter sputorum",
    "camu"	: "Campylobacter upsaliensis",
    "cana"	: "Candida albicans",
    "cang"	: "Candida glabrata",
    "cank"	: "Candida krusei",
    "cant"	: "Candida tropicalis",
    "cals"	: "Candidatus Liberibacter solanacearum",
    "carm"	: "Carnobacterium maltaromaticum",
    "chls"	: "Chlamydiales spp.",
    "citf"	: "Citrobacter freundii",
    "clos"	: "Clonorchis sinensis",
    "clob"	: "Clostridium botulinum",
    "clod"	: "Clostridium difficile",
    "mcum"	: "Clostridium septicum",
    "cord"	: "Corynebacterium diphtheriae",
    "cros"	: "Cronobacter spp.",
    "dicn"	: "Dichelobacter nodosus",
    "edws"	: "Edwardsiella spp.",
    "entc"	: "Enterobacter cloacae",
    "entf"	: "Enterococcus faecalis",
    "sium"	: "Enterococcus faecium",
    "escc1"	: "Escherichia coli#1",
    "escc2"	: "Escherichia coli#2",
    "flap"	: "Flavobacterium psychrophilum",
    "gala"	: "Gallibacterium anatis",
    "haei"	: "Haemophilus influenzae",
    "haep"	: "Haemophilus parasuis",
    "helc"	: "Helicobacter cinaedi",
    "help"	: "Helicobacter pylori",
    "hels"	: "Helicobacter suis",
    "kink"	: "Kingella kingae",
    "klea"	: "Klebsiella aerogenes",
    "kleo"	: "Klebsiella oxytoca",
    "klep"	: "Klebsiella pneumoniae",
    "kuds"	: "Kudoa septempunctata",
    "lacs"	: "Lactobacillus salivarius",
    "leps"	: "Leptospira spp.",
    "leps2"	: "Leptospira spp.#2",
    "leps3"	: "Leptospira spp.#3",
    "lism"	: "Listeria monocytogenes",
    "macc"	: "Macrococcus canis",
    "scus"	: "Macrococcus caseolyticus",
    "manh"	: "Mannheimia haemolytica",
    "melp"	: "Melissococcus plutonius",
    "morc"	: "Moraxella catarrhalis",
    "mycs"	: "Mycobacteria spp.",
    "myca"	: "Mycobacterium abscessus",
    "mycm"	: "Mycobacterium massiliense",
    "mycoa"	: "Mycoplasma agalactiae",
    "mycb"	: "Mycoplasma bovis",
    "mych"	: "Mycoplasma hyopneumoniae",
    "anis"	: "Mycoplasma hyorhinis",
    "myci"	: "Mycoplasma iowae",
    "mycp"	: "Mycoplasma pneumoniae",
    "mycos"	: "Mycoplasma synoviae",
    "neis"	: "Neisseria spp.",
    "orit"	: "Orientia tsutsugamushi",
    "ornr"	: "Ornithobacterium rhinotracheale",
    "pael"	: "Paenibacillus larvae",
    "pasm1"	: "Pasteurella multocida#1",
    "pasm2"	: "Pasteurella multocida#2",
    "pedp"	: "Pediococcus pentosaceus",
    "phod"	: "Photobacterium damselae",
    "piss"	: "Piscirickettsia salmonis",
    "porg"	: "Porphyromonas gingivalis",
    "proa"	: "Propionibacterium acnes",
    "psea"	: "Pseudomonas aeruginosa",
    "psef"	: "Pseudomonas fluorescens",
    "psep"	: "Pseudomonas putida",
    "rhos"	: "Rhodococcus spp.",
    "riea"	: "Riemerella anatipestifer",
    "sale"	: "Salmonella enterica",
    "sapp"	: "Saprolegnia parasitica",
    "sins"	: "Sinorhizobium spp.",
    "staa"	: "Staphylococcus aureus",
    "stae"	: "Staphylococcus epidermidis",
    "stah"	: "Staphylococcus haemolyticus",
    "snis"	: "Staphylococcus hominis",
    "stal"	: "Staphylococcus lugdunensis",
    "stap"	: "Staphylococcus pseudintermedius",
    "stem"	: "Stenotrophomonas maltophilia",
    "stra"	: "Streptococcus agalactiae",
    "sbcx"	: "Streptococcus bovis/equinus complex (SBSEC)",
    "strc"	: "Streptococcus canis",
    "stde"	: "Streptococcus dysgalactiae equisimilis",
    "strg"	: "Streptococcus gallolyticus",
    "stro"	: "Streptococcus oralis",
    "strp"	: "Streptococcus pneumoniae",
    "snes"	: "Streptococcus pyogenes",
    "strs"	: "Streptococcus suis",
    "strt"	: "Streptococcus thermophilus",
    "strt2"	: "Streptococcus thermophilus#2",
    "stru"	: "Streptococcus uberis",
    "strz"	: "Streptococcus zooepidemicus",
    "sspp"	: "Streptomyces spp",
    "tays"	: "Taylorella spp.",
    "tens"	: "Tenacibaculum spp.",
    "trep"	: "Treponema pallidum",
    "triv"	: "Trichomonas vaginalis",
    "ures"	: "Ureaplasma spp.",
    "vibc"	: "Vibrio cholerae",
    "vibc2"	: "Vibrio cholerae#2",
    "vibp"	: "Vibrio parahaemolyticus",
    "vibs"	: "Vibrio spp.",
    "vibt"	: "Vibrio tapetis",
    "vibv"	: "Vibrio vulnificus",
    "wolb"	: "Wolbachia",
    "xylf"	: "Xylella fastidiosa",
    "yerp"	: "Yersinia pseudotuberculosis",
    "yerr"	: "Yersinia ruckeri",
    "yers"	: "Yersinia spp."
}


genes_dict = {
    "card" : "CARD",
    "resfinder" : "Resfinder",
    "plasmidfinder" : "Plasmidfinder",
    "megares" : "Megares",
    "argannot" : "Argannot",
    "vfdb_core" : "vfdb_core",
    "vfdb_full" : "vfdb_full",
    "virulencefinder" : "virulencefinder"
}

def run_ariba(cmd):
    _cmd = shlex.split(cmd)
    subprocess.check_call(_cmd)

def build_mlst(mlst_db):
    mlst_species = mlst_dict[mlst_db]
    run_ariba("ariba pubmlstget '{}' out".format(mlst_species))
    output_path = os.getcwd()
    old = "{}/out/ref_db".format(output_path, mlst_db)
    new = "{}/{}".format(output_path, mlst_db)
    shutil.move(old, new)

def build_curated_db(gen_db):
    run_ariba("ariba getref {} out".format(gen_db))
    run_ariba("ariba prepareref -f out.fa -m out.tsv {}".format(gen_db))

def build_custom_db(fasta, coding, db_name):
    run_ariba("ariba prepareref --all_coding {} -f {} {}".format(coding, fasta, db_name))

def _add_data_table_entry(data_manager_dict, data_table_name, data_table_entry):
    data_manager_dict['data_tables'] = data_manager_dict.get( 'data_tables', {} )
    data_manager_dict['data_tables'][ data_table_name ] = data_manager_dict['data_tables'].get( data_table_name, [] )
    data_manager_dict['data_tables'][ data_table_name ].append( data_table_entry )
    return data_manager_dict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('params')
    parser.add_argument( '-t', '--dbtype', dest='database_type', help='database type' )
    parser.add_argument( '-d', '--db', dest='db_name', help='database name' )
    parser.add_argument( '-c', '--coding', dest='coding', help='' )
    parser.add_argument( '-f', '--fasta', dest='fasta', help='' )
    args = parser.parse_args()

    if args.database_type == "curated":
        build_curated_db(args.db_name)
        name = genes_dict[args.db_name]
    elif args.database_type == "mlst":
        build_mlst(args.db_name)
        name = mlst_dict[args.db_name]
    elif args.database_type == "fasta":
        build_custom_db(args.fasta, args.coding, args.db_name)
        name = args.db_name

    params = json.loads(open(args.params).read())
    pprint(params)    
    target_directory = params['output_data'][0]['extra_files_path']
    
    if not os.path.isdir(target_directory):
      os.mkdir(target_directory)

    output_path = os.getcwd()
    shutil.copytree(os.path.join(output_path, args.db_name), os.path.join(target_directory, args.db_name))
    
    data_manager_dict = {}

    data_table_entry = {
        "value": args.db_name,
        "name": name,
        "path": os.path.join(target_directory, args.db_name)
    }
    _add_data_table_entry(data_manager_dict, data_table_name, data_table_entry)
    open(args.params, 'wb').write(json.dumps(data_manager_dict))

if __name__ == "__main__":
    main()
