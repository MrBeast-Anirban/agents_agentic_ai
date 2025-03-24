from sentence_transformers import SentenceTransformer, util

class TextSimilarity:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Load a pre-trained model

    def calculate_similarity(self, text1, text2):
        """
        Calculate the similarity between two texts using Sentence Transformers.
        
        :param text1: The first text.
        :param text2: The second text.
        :return: Similarity score (0 to 1).
        """
        try:
            # Encode the texts
            embeddings = self.model.encode([text1, text2], convert_to_tensor=True)
            # Calculate cosine similarity
            similarity = util.cos_sim(embeddings[0], embeddings[1])
            return similarity.item()
        except Exception as e:
            return f"Error calculating similarity: {e}"