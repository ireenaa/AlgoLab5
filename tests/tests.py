# import unittest
# from src.main import dfs
#
# def calculate_max_experience(company_structure):
#     memory = {}
#     return dfs(0, 0, company_structure, memory)
#
# class TestMaxExperience(unittest.TestCase):
#
#     def test_example_1(self):
#         company_structure = [
#             [4],
#             [3, 1],
#             [2, 1, 5],
#             [1, 3, 2, 1]
#         ]
#         self.assertEqual(calculate_max_experience(company_structure), 12)
#
#     def test_example_2(self):
#         company_structure = [
#             [9999]
#         ]
#         self.assertEqual(calculate_max_experience(company_structure), 9999)
#
#     def test_example_3(self):
#         company_structure = [
#             [0],
#             [1, 1],
#             [0, 0, 0],
#             [1, 1, 1, 1],
#             [0, 1, 0, 1, 0]
#         ]
#         self.assertEqual(calculate_max_experience(company_structure), 3)
#
#     def test_empty_company(self):
#         company_structure = [[]]
#         self.assertEqual(calculate_max_experience(company_structure), 0)
#
#     def test_single_level_company(self):
#         company_structure = [[5]]
#         self.assertEqual(calculate_max_experience(company_structure), 5)
#
#     def test_large_company(self):
#         company_structure = [[i for i in range(j)] for j in range(1, 101)]
#         self.assertEqual(calculate_max_experience(company_structure), 4950)
#
# if __name__ == '__main__':
#     unittest.main()
