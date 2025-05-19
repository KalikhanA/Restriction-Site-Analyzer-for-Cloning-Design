from Bio import SeqIO
from Bio.Restriction import RestrictionBatch, Analysis
from Bio.Seq import Seq

def check_enzymes_for_cloning(mcs_sequence, insert_sequence, enzyme_names, added_sites=None):
    
    full_insert = insert_sequence
    if added_sites:
        for site in added_sites.values():
            full_insert = site + full_insert  

    mcs_seq = Seq(mcs_sequence)
    insert_seq = Seq(full_insert)

    enzymes = RestrictionBatch(enzyme_names)

    print("\n--- MCS Analysis ---")
    mcs_analysis = Analysis(enzymes, mcs_seq)
    mcs_analysis.print_that()

    print("\n--- Insert Analysis ---")
    insert_analysis = Analysis(enzymes, insert_seq)
    insert_analysis.print_that()


mcs_sequence =  "your multiple cloning site"
insert_sequence = sequence = """ your insert sequence (plasmid)"""



enzyme_names = ["For example:" 'EcoRI', 'BamHI', 'XbaI', 'HindIII', 'ApaI', 'KpnI', 'NotI', 'Acc65I', 'SnaBI', 'PstI', 'BglII', 'SmaI', 'NdeI']

check_enzymes_for_cloning(mcs_sequence, insert_sequence, enzyme_names)


