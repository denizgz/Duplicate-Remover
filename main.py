from DuplicateRemover import DuplicateRemover

dirname = "mercedes-benz-1-nov-cleaning - Kopie\Mercedes-Benz V-Class 2014"

# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# Find Similar Images
#dr.find_similar("IMG-20110704-00007.jpg",70)