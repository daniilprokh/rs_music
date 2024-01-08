import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.preprocessing import normalize

class RecommendationSystem():
    def __init__(self):
        interactions_df = pd.read_csv("dataset/lastfm_user_scrobbles.csv")
        titles_df = pd.read_csv("dataset/lastfm_artist_list.csv")

        titles_df.index = titles_df["artist_id"]
        self.m_artist_title_by_id_ = titles_df["artist_name"].to_dict()
        titles_df.index = titles_df["artist_name"]
        self.m_artist_id_by_title_ = titles_df["artist_id"].to_dict()

        # получаем матрицу UI
        rows, r_pos = np.unique(interactions_df.values[:,0], return_inverse=True)
        cols, c_pos = np.unique(interactions_df.values[:,1], return_inverse=True)
        self.m_interactions_sparse_ = sparse.csr_matrix((interactions_df.values[:,2],
                                                        (r_pos, c_pos)))

        # нормализуем и получаем матрицу похожести
        Pui = normalize(self.m_interactions_sparse_)
        self.m_sim_ = Pui.T * Pui

        # предсказания для пользователей
        interactions_sparse_transpored = self.m_interactions_sparse_.transpose(copy=True)
        Piu = normalize(interactions_sparse_transpored)
        self.m_fit_ = Pui * Piu * Pui

    def GetPrefferedArtistTitles(self, user_id: int):
        return set([self.m_artist_title_by_id_[id + 1] for id in np.nonzero(self.m_interactions_sparse_[user_id])[1].tolist()])

    def GetRecommendedArtistTitles(self, user_id: int):
        preffered = self.GetPrefferedArtistTitles(user_id)
        recommended = set([self.m_artist_title_by_id_[id + 1] for id in self.m_fit_[user_id].toarray().argsort()[0][-20:]])
        return recommended - preffered

    def GetSimilarArtists(self, artist_title: str):
        if artist_title not in self.m_artist_id_by_title_:
            return
        artist_id = self.m_artist_id_by_title_[artist_title] - 1
        artists = set([self.m_artist_title_by_id_[id + 1] for id in self.m_sim_[artist_id].toarray().argsort()[0][-20:]])
        artists.remove(artist_title)
        return artists
