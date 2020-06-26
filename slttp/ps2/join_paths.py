partial_paths=input().split(',')
partial_paths=[i.strip() for i in partial_paths]
final_path='/'.join(partial_paths)

print(final_path)