import numpy as np
from rf_word2vec import W2VResumeFilter

def al_otaibi_resume_filter(users_fname, jobs_fname):
    """ Al Otaibi method """

    print("# -- Al Otaibi Resume Filter -- #")
    w2vrf = W2VResumeFilter(debiased=False, initialize=False)
    print("Loaded models")

    # Load users
    users = w2vrf.load_candidates(users_fname)
    user_genders = users['genders']
    user_profiles = []
    for user in users['candidates']:
        user_profiles.append(user[:7])
    user_vectors = [[int(u) for u in user] for user in user_profiles]

    # Load jobs
    job_profiles = w2vrf.load_jobs(jobs_fname)
    job_vectors = [np.ones(7) for j in job_profiles]


    cosine_job_ranks = []
    for job_vector in job_vectors:
        ranks = w2vrf.cosine_filter_candidates(user_vectors, job_vector)
        cosine_job_ranks.append(ranks)
        print("cosine:", ranks)

    euclidean_job_ranks = []
    for job_vector in job_vectors:
        ranks = w2vrf.euclidean_filter_candidates(user_vectors, job_vector)
        euclidean_job_ranks.append(ranks)
        print("euclidean:", ranks)

    jaccard_job_ranks = []
    for job_vector in job_vectors:
        ranks = w2vrf.jaccard_filter_candidates(user_vectors, job_vector)
        jaccard_job_ranks.append(ranks)
        print("jaccard:", ranks)

    a = np.asarray(cosine_job_ranks, dtype=int)
    ag = [[user_genders[i] for i in job_rank] for job_rank in cosine_job_ranks]
    b = np.asarray(euclidean_job_ranks, dtype=int)
    bg = [[user_genders[i] for i in job_rank] for job_rank in euclidean_job_ranks]
    c = np.asarray(jaccard_job_ranks, dtype=int)
    cg = [[user_genders[i] for i in job_rank] for job_rank in jaccard_job_ranks]
    np.savetxt("./data/_cosine_genders_alotaibi.csv", ag, delimiter=",", fmt="%s")
    np.savetxt("./data/_euclidean_genders_alotaibi.csv", bg, delimiter=",", fmt="%s")
    np.savetxt("./data/_jaccard_genders_alotaibi.csv", cg, delimiter=",", fmt="%s")
    np.savetxt("./data/_cosine_ranks_alotaibi.csv", a, delimiter=",", fmt="%s")
    np.savetxt("./data/_euclidean_ranks_alotaibi.csv", b, delimiter=",", fmt="%s")
    np.savetxt("./data/_jaccard_ranks_alotaibi.csv", c, delimiter=",", fmt="%s")


def w2v_resume_filter(users_fname, jobs_fname, debiased=False):
    """ W2V method """

    print("# -- Word2Vec -- #")
    w2vrf = W2VResumeFilter(debiased=debiased)
    print("Loaded models")

    # Load users
    users = w2vrf.load_candidates(users_fname)
    user_genders = users['genders']
    user_profiles = []
    for user in users['candidates']:
        user_profiles.append(user[8:])
    user_vectors = [w2vrf.get_word_centroid_vec(u) for u in user_profiles]

    # Load jobs
    job_profiles = w2vrf.load_jobs(jobs_fname)
    job_vectors = [w2vrf.get_word_centroid_vec(j) for j in job_profiles]

    cosine_job_ranks = []
    for job_vector in job_vectors:
        ranks = w2vrf.cosine_filter_candidates(user_vectors, job_vector)
        cosine_job_ranks.append(ranks)
        print("cosine:", ranks)

    euclidean_job_ranks = []
    for job_vector in job_vectors:
        ranks = w2vrf.euclidean_filter_candidates(user_vectors, job_vector)
        euclidean_job_ranks.append(ranks)
        print("euclidean:", ranks)

    jaccard_job_ranks = []
    for job_string in job_profiles:
        ranks = w2vrf.jaccard_filter_candidates(user_profiles, job_string)
        jaccard_job_ranks.append(ranks)
        print("jaccard:", ranks)


    a = np.asarray(cosine_job_ranks, dtype=int)
    ag = [[user_genders[i] for i in job_rank] for job_rank in cosine_job_ranks]
    b = np.asarray(euclidean_job_ranks, dtype=int)
    bg = [[user_genders[i] for i in job_rank] for job_rank in euclidean_job_ranks]
    c = np.asarray(jaccard_job_ranks, dtype=int)
    cg = [[user_genders[i] for i in job_rank] for job_rank in jaccard_job_ranks]
    np.savetxt("./data/" + str(debiased) + "_cosine_ranks_g.csv", ag, delimiter=",", fmt="%s")
    np.savetxt("./data/" + str(debiased) + "_euclidean_ranks_g.csv", bg, delimiter=",", fmt="%s")
    np.savetxt("./data/" + str(debiased) + "_jaccard_ranks_g.csv", cg, delimiter=",", fmt="%s")
    np.savetxt("./data/" + str(debiased) + "_cosine_ranks.csv", a, delimiter=",", fmt="%s")
    np.savetxt("./data/" + str(debiased) + "_euclidean_ranks.csv", b, delimiter=",", fmt="%s")
    np.savetxt("./data/" + str(debiased) + "_jaccard_ranks.csv", c, delimiter=",", fmt="%s")

def main():
    """ Main method """
    user_fname = "updated_user_profiles.csv"
    jobs_fname = "job_descriptions.csv"
    w2v_resume_filter(users_fname=user_fname, jobs_fname=jobs_fname, debiased=False)
    w2v_resume_filter(users_fname=user_fname, jobs_fname=jobs_fname, debiased=True)
    al_otaibi_resume_filter(user_fname, jobs_fname)

if __name__ == "__main__":
    main()
