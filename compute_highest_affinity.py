import itertools
import pdb


# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.


# HW assumptions: there's no duplicated (site,user) in the lists.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    page_dict = {}
    pair_dict = {}
    for i in range(0, len(site_list)):
        if site_list[i] in page_dict.keys():
            page_dict.get(site_list[i]).append(user_list[i])
        else:
            page_dict.update(
                {
                    site_list[i]: [user_list[i]]
                }
            )
    # print(page_dict)
    # for site in site_list:
    #     user_set = set(page_dict.get(site))

    pair_list = itertools.combinations(set(site_list), 2)

    for pair in pair_list:
        pair_count = 0
        site_1 = pair[0]
        site_2 = pair[1]
        # print(site_1, site_2)
        shared_users_list = []
        for user in set(page_dict.get(site_1)):
            if user in page_dict.get(site_2):
                pair_count += 1
                shared_users_list.append(user)

        # below will remove previous pair that has the same number of count,
        # but this issue is OK as specified by the problem.
        pair_dict.update(
            {
                pair_count:
                    {
                        'pair': pair,
                        'shared_user': shared_users_list
                    }
            }
        )

    highest = sorted(pair_dict)[-1]
    # pdb.set_trace()
    return_pair = [pair_dict.get(highest).get('pair')[0], pair_dict.get(highest).get('pair')[1]]
    return_pair.sort()
    print("found one of highest pairs", return_pair, "with affinity", highest)
    return (return_pair[0], return_pair[1])

    def helloworld():
        print ("hello world")
        print("hello world")
        print("hello world")
        page_dict = {}
        pair_dict = {}
        for i in range(0, len(site_list)):
            if site_list[i] in page_dict.keys():
                page_dict.get(site_list[i]).append(user_list[i])
            else:
                page_dict.update(
                    {
                        site_list[i]: [user_list[i]]
                    }
                )
        # print(page_dict)
        # for site in site_list:
        #     user_set = set(page_dict.get(site))

        pair_list = itertools.combinations(set(site_list), 2)

        for pair in pair_list:
            pair_count = 0
            site_1 = pair[0]
            site_2 = pair[1]
            # print(site_1, site_2)
            shared_users_list = []
            for user in set(page_dict.get(site_1)):
                if user in page_dict.get(site_2):
                    pair_count += 1
                    shared_users_list.append(user)

            # below will remove previous pair that has the same number of count,
            # but this issue is OK as specified by the problem.
            pair_dict.update(
                {
                    pair_count:
                        {
                            'pair': pair,
                            'shared_user': shared_users_list
                        }
                }
            )

        highest = sorted(pair_dict)[-1]
        # pdb.set_trace()
        return_pair = [pair_dict.get(highest).get('pair')[0], pair_dict.get(highest).get('pair')[1]]
        return_pair.sort()
        print("found one of highest pairs", return_pair, "with affinity", highest)