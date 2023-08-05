import os
from logging import getLogger, INFO
import time
import openai
import asyncio
from pathlib import Path
log = getLogger(__name__)
log.setLevel(INFO)


class GPT4(object):
    def __init__(self, key=None, model='gpt-4', temperature=0.8, top_p=1, presence_penalty=0, frequency_penalty=0, n=1, stream=False, system_content=None):
        if os.environ.get("OPENAI_API_KEY") is None:
            if key:
                openai.api_key = key
        self.model = model
        self.temperature = temperature
        # 用于控制生成文本的随机性和创造性的参数。值越高，生成文本越随机和创造性；值越低，生成文本越可预测和保守
        self.top_p = top_p
        # 用于对生成文本进行选择的参数，它表示只选择所有可能的令牌中累计概率高于给定阈值的那些令牌。默认值为1，表示选择所有可能的令牌
        self.presence_penalty = presence_penalty
        # 用于惩罚生成文本中未出现过的片段的参数。默认值为0，表示不进行惩罚
        self.frequency_penalty = frequency_penalty
        # 用于惩罚生成文本中频繁出现的重复片段的参数。默认值为0，表示不进行惩罚
        self.n = n
        # 要生成的文本的数量。默认为1，表示生成一段文本
        self.stream = stream
        # 是否将生成的文本作为流返回，而不是一次性返回所有文本。默认为False，表示一次性返回所有文本
        self.system_content = system_content or "一个拥有20年经验的c++程序员，帮助分析代码问题"
        self.messages = [
            {"role": "system", "content": self.system_content}
        ]

    @staticmethod
    def read_prompt(path):
        return Path(path).read_text()

    def asyncio_run_gpt_ask(self, prompt, realTime_output=False):
        if len(self.messages) == 0:
            self.messages.append({"role": "system", "content": self.system_content})
        self.messages.append({"role": "user", "content": prompt})
        if realTime_output:
            print("## You")
            print(prompt)
            print("## chatGPT")
        if self.stream:
            return asyncio.run(self.__ask(realTime_output))[0]
        else:
            start_time = time.time()
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature
            )
            elapsed_time = time.time() - start_time
            return response['choices'][0]['message']['content'], int(round(elapsed_time, 0))

    async def __ask(self, realTime_output=False):
        return await asyncio.gather(*[self.__generate_text_async(realTime_output)])

    async def __generate_text_async(self, realTime_output) -> tuple:
        response_text_array = []
        response_text = ""
        start_time = time.time()
        async for chunk in await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self.messages,
            # max_tokens=7000,
            temperature=self.temperature,
            top_p=self.top_p,
            # timeout=600,
            presence_penalty=self.presence_penalty,
            frequency_penalty=self.frequency_penalty,
            n=self.n,
            stream=self.stream
        ):
            chunk = chunk['choices'][0]
            if "content" in chunk["delta"]:
                text = chunk["delta"]['content']
                response_text += text
                if text in ["\n"]:
                    response_text_array.append(response_text)
                    if realTime_output:
                        print(response_text)
                    response_text = ""
        elapsed_time = time.time() - start_time
        log.info(f"{elapsed_time:.2f} seconds to execute")
        return "\n".join(response_text_array), int(round(elapsed_time, 0))