# config.py
DB_FILE = "chat_feedback.db"

# Model leaderboard
# https://wandb.ai/llm-jp-eval/open-llm-leaderboard/reports/-Open-LLM-Leaderboard--Vmlldzo2MTE0NDA3
# https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard
# https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

# MODEL_NAME = "google/gemma-2-2b-jpn-it"
# MODEL_NAME = "google/gemma-3-27b-it"
# →モデルが大きすぎてGPUに乗らない
# MODEL_NAME = "google/gemma-3-1b-pt"
# →pretrainingモデル (pt)にはトークナイザーにチャットテンプレートがない
MODEL_NAME = "google/gemma-3-1b-it"