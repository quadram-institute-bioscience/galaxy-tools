# Thanh Le Viet
# 7-Jan-2019

import argparse
import json
import os
import shutil


mlst_dict = {
    "Achromobacter_spp.":"Achromobacter spp.",
    "Acinetobacter_baumannii_1":"Acinetobacter baumannii#1",
    "Acinetobacter_baumannii_2":"Acinetobacter baumannii#2",
    "Aeromonas_spp.":"Aeromonas spp.",
    "Anaplasma_phagocytophilum":"Anaplasma phagocytophilum",
    "Arcobacter_spp.":"Arcobacter spp.",
    "Aspergillus_fumigatus":"Aspergillus fumigatus",
    "Bacillus_cereus":"Bacillus cereus",
    "Bacillus_licheniformis":"Bacillus licheniformis",
    "Bacillus_subtilis":"Bacillus subtilis",
    "Bartonella_bacilliformis":"Bartonella bacilliformis",
    "Bartonella_henselae":"Bartonella henselae",
    "Bordetella_spp.":"Bordetella spp.",
    "Borrelia_spp.":"Borrelia spp.",
    "Brachyspira_hampsonii":"Brachyspira hampsonii",
    "Brachyspira_hyodysenteriae":"Brachyspira hyodysenteriae",
    "Brachyspira_intermedia":"Brachyspira intermedia",
    "Brachyspira_pilosicoli":"Brachyspira pilosicoli",
    "Brachyspira_spp.":"Brachyspira spp.",
    "Brucella_spp.":"Brucella spp.",
    "Burkholderia_cepacia_complex":"Burkholderia cepacia complex",
    "Burkholderia_pseudomallei":"Burkholderia pseudomallei",
    "Campylobacter_concisus_curvus":"Campylobacter concisus/curvus",
    "Campylobacter_fetus":"Campylobacter fetus",
    "Campylobacter_helveticus":"Campylobacter helveticus",
    "Campylobacter_hyointestinalis":"Campylobacter hyointestinalis",
    "Campylobacter_insulaenigrae":"Campylobacter insulaenigrae",
    "Campylobacter_jejuni":"Campylobacter jejuni",
    "Campylobacter_lanienae":"Campylobacter lanienae",
    "Campylobacter_lari":"Campylobacter lari",
    "Campylobacter_sputorum":"Campylobacter sputorum",
    "Campylobacter_upsaliensis":"Campylobacter upsaliensis",
    "Candida_albicans":"Candida albicans",
    "Candida_glabrata":"Candida glabrata",
    "Candida_krusei":"Candida krusei",
    "Candida_tropicalis":"Candida tropicalis",
    "Carnobacterium_maltaromaticum":"Carnobacterium maltaromaticum",
    "Chlamydiales_spp.":"Chlamydiales spp.",
    "Citrobacter_freundii":"Citrobacter freundii",
    "Clonorchis_sinensis":"Clonorchis sinensis",
    "Clostridium_botulinum":"Clostridium botulinum",
    "Clostridium_difficile":"Clostridium difficile",
    "Clostridium_septicum":"Clostridium septicum",
    "Corynebacterium_diphtheriae":"Corynebacterium diphtheriae",
    "Cronobacter_spp.":"Cronobacter spp.",
    "Dichelobacter_nodosus":"Dichelobacter nodosus",
    "Edwardsiella_spp.":"Edwardsiella spp.",
    "Enterobacter_cloacae":"Enterobacter cloacae",
    "Enterococcus_faecalis":"Enterococcus faecalis",
    "Enterococcus_faecium":"Enterococcus faecium",
    "Escherichia_coli_1":"Escherichia coli#1",
    "Escherichia_coli_2":"Escherichia coli#2",
    "Flavobacterium_psychrophilum":"Flavobacterium psychrophilum",
    "Gallibacterium_anatis":"Gallibacterium anatis",
    "Haemophilus_influenzae":"Haemophilus influenzae",
    "Haemophilus_parasuis":"Haemophilus parasuis",
    "Helicobacter_cinaedi":"Helicobacter cinaedi",
    "Helicobacter_pylori":"Helicobacter pylori",
    "Helicobacter_suis":"Helicobacter suis",
    "Kingella_kingae":"Kingella kingae",
    "Klebsiella_aerogenes":"Klebsiella aerogenes",
    "Klebsiella_oxytoca":"Klebsiella oxytoca",
    "Klebsiella_pneumoniae":"Klebsiella pneumoniae",
    "Kudoa_septempunctata":"Kudoa septempunctata",
    "Lactobacillus_salivarius":"Lactobacillus salivarius",
    "Leptospira_spp.":"Leptospira spp.",
    "Leptospira_spp._2":"Leptospira spp.#2",
    "Leptospira_spp._3":"Leptospira spp.#3",
    "Listeria_monocytogenes":"Listeria monocytogenes",
    "Macrococcus_canis":"Macrococcus canis",
    "Macrococcus_caseolyticus":"Macrococcus caseolyticus",
    "Mannheimia_haemolytica":"Mannheimia haemolytica",
    "Melissococcus_plutonius":"Melissococcus plutonius",
    "Moraxella_catarrhalis":"Moraxella catarrhalis",
    "Mycobacteria_spp.":"Mycobacteria spp.",
    "Mycobacterium_abscessus":"Mycobacterium abscessus",
    "Mycobacterium_massiliense":"Mycobacterium massiliense",
    "Mycoplasma_agalactiae":"Mycoplasma agalactiae",
    "Mycoplasma_bovis":"Mycoplasma bovis",
    "Mycoplasma_hyopneumoniae":"Mycoplasma hyopneumoniae",
    "Mycoplasma_hyorhinis":"Mycoplasma hyorhinis",
    "Mycoplasma_iowae":"Mycoplasma iowae",
    "Mycoplasma_pneumoniae":"Mycoplasma pneumoniae",
    "Mycoplasma_synoviae":"Mycoplasma synoviae",
    "Neisseria_spp.":"Neisseria spp.",
    "Orientia_tsutsugamushi":"Orientia tsutsugamushi",
    "Ornithobacterium_rhinotracheale":"Ornithobacterium rhinotracheale",
    "Paenibacillus_larvae":"Paenibacillus larvae",
    "Pasteurella_multocida_1":"Pasteurella multocida#1",
    "Pasteurella_multocida_2":"Pasteurella multocida#2",
    "Pediococcus_pentosaceus":"Pediococcus pentosaceus",
    "Photobacterium_damselae":"Photobacterium damselae",
    "Piscirickettsia_salmonis":"Piscirickettsia salmonis",
    "Porphyromonas_gingivalis":"Porphyromonas gingivalis",
    "Propionibacterium_acnes":"Propionibacterium acnes",
    "Pseudomonas_aeruginosa":"Pseudomonas aeruginosa",
    "Pseudomonas_fluorescens":"Pseudomonas fluorescens",
    "Pseudomonas_putida":"Pseudomonas putida",
    "Rhodococcus_spp.":"Rhodococcus spp.",
    "Riemerella_anatipestifer":"Riemerella anatipestifer",
    "Salmonella_enterica":"Salmonella enterica",
    "Saprolegnia_parasitica":"Saprolegnia parasitica",
    "Sinorhizobium_spp.":"Sinorhizobium spp.",
    "Staphylococcus_aureus":"Staphylococcus aureus",
    "Staphylococcus_epidermidis":"Staphylococcus epidermidis",
    "Staphylococcus_haemolyticus":"Staphylococcus haemolyticus",
    "Staphylococcus_hominis":"Staphylococcus hominis",
    "Staphylococcus_lugdunensis":"Staphylococcus lugdunensis",
    "Staphylococcus_pseudintermedius":"Staphylococcus pseudintermedius",
    "Stenotrophomonas_maltophilia":"Stenotrophomonas maltophilia",
    "Streptococcus_agalactiae":"Streptococcus agalactiae",
    "Streptococcus_bovis_equinus_complex__SBSEC_":"Streptococcus bovis/equinus complex (SBSEC)",
    "Streptococcus_canis":"Streptococcus canis",
    "Streptococcus_dysgalactiae_equisimilis":"Streptococcus dysgalactiae equisimilis",
    "Streptococcus_gallolyticus":"Streptococcus gallolyticus",
    "Streptococcus_oralis":"Streptococcus oralis",
    "Streptococcus_pneumoniae":"Streptococcus pneumoniae",
    "Streptococcus_pyogenes":"Streptococcus pyogenes",
    "Streptococcus_suis":"Streptococcus suis",
    "Streptococcus_thermophilus":"Streptococcus thermophilus",
    "Streptococcus_thermophilus_2":"Streptococcus thermophilus#2",
    "Streptococcus_uberis":"Streptococcus uberis",
    "Streptococcus_zooepidemicus":"Streptococcus zooepidemicus",
    "Streptomyces_spp":"Streptomyces spp",
    "Taylorella_spp.":"Taylorella spp.",
    "Tenacibaculum_spp.":"Tenacibaculum spp.",
    "Treponema_pallidum":"Treponema pallidum",
    "Trichomonas_vaginalis":"Trichomonas vaginalis",
    "Ureaplasma_spp.":"Ureaplasma spp.",
    "Vibrio_cholerae":"Vibrio cholerae",
    "Vibrio_cholerae_2":"Vibrio cholerae#2",
    "Vibrio_parahaemolyticus":"Vibrio parahaemolyticus",
    "Vibrio_spp.":"Vibrio spp.",
    "Vibrio_tapetis":"Vibrio tapetis",
    "Vibrio_vulnificus":"Vibrio vulnificus",
    "Wolbachia":"Wolbachia",
    "Xylella_fastidiosa":"Xylella fastidiosa",
    "Yersinia_pseudotuberculosis":"Yersinia pseudotuberculosis",
    "Yersinia_ruckeri":"Yersinia ruckeri",
    "Yersinia_spp.":"Yersinia spp."
}

def main(args):
    output_path = os.getcwd()
    db_folder = [d for d in os.listdir(output_path) if os.path.isdir(d)]
    params = json.loads(open(args.output).read())
    target_directory = params['output_data'][0]['extra_files_path']
    os.mkdir(target_directory)
    data_manager_entry = []
    for db in db_folder:
        print("Current: ".format(os.path.join(output_path, d)))
        print("Target: {}".format(target_directory))
        shutil.move(os.path.join(output_path, d), os.path.join(target_directory, d))
        data_manager_entry.append(dict(value=db.lower(),
                                  name=mlst_dict[db],
                                  path=target_directory)
                                    )
    data_manager_json = dict(data_tables=dict(ariba_databases=data_manager_entry))
    file(args.output, 'w').write(json.dumps(data_manager_json))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create data manager json.')
    parser.add_argument('--out', dest='output', action='store', help='JSON filename')
    args = parser.parse_args()
    main(args)