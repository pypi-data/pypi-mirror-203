# -*- coding: utf-8 -*-
import json
import os
import requests
from bs4 import BeautifulSoup as bs
import re
from time import time, sleep
import random
import numpy as np
import traceback
import datetime
from isqmap import transpile
from qcistoqasm.qcis_to_qasm import QcisToQasm
from qasmtoqcis.qasm_to_qcis import QasmToQcis
from sabreMapper.sabre_mapper import SabreMapper
from typing import List, Optional, Dict


class Account():

    def __init__(
            self,
            username: Optional[str]=None,
            password: Optional[str]=None,
            login_key: Optional[str]=None,
            machine_name: Optional[str]=None,
            exp: Optional[str]=None,
            full_expr_record: Optional[str]=False
        ):
        """accout initialization, 
           entering user name and password calls oneD12 quantum computer,
           entering login key can call quantum computer other than oneD12,
           but you need to set the name of quantum computer at this time.

        Args:
            username: 
                username. Defaults to None.
            password: 
                password. Defaults to None.
            login_key: 
                SDK key under personal center on the web. Defaults to None.
            machine_name: 
                name of quantum computer. Defaults to None.
            exp: 
                oneD12, Historical experimental records stored locally. Defaults to None.
            full_expr_record: 
                oneD12, append or overwrite in local records. Defaults to False.

        Raises:
            Exception: throw an exception when login fails
        """
        self.qasmtoqcis = QasmToQcis()
        self.qcistoqasm = QcisToQasm()
        self.username = username
        self.password = password
        self.login_key = login_key
        self.token = None
        if exp is None:
            self.exp = {}
        else:
            self.exp = exp
        self.machine_name = machine_name
        self.full_expr_record = full_expr_record
        if self.login_key:
            cloud_url = 'https://quantumcomputer.ac.cn/'
            self.base_url = f'{cloud_url}'
            self.login = self.log_in()
        else:
            self.cloud_url = 'https://quantumcomputer.ac.cn'
            self.base_url = f'{self.cloud_url}/pyRequest?username={username}&password={password}'
            self.login = self.log_in()
            if self.machine_name:
                self.set_machine(self.machine_name)
        if self.login == 0:
            raise Exception('登录失败')

    def log_in(self):
        """Authenticate username and password and return user credit

        Returns:
            int: log in state, 1 means pass authentication, 0 means failed

        """
        if self.login_key:
            url = f'{self.base_url}/sdk/api/multiple/experiment/login'
            data = {"loginToken": self.login_key}
            res = requests.post(url, json=data)
            status_code = res.status_code
            if status_code != 200:
                return 0
            result = json.loads(res.text)
            code = result.get('code', -1)
            msg = result.get('msg', '登录失败')
            if code != 0:
                print(f'登录失败：{msg}')
                return 0
            token = result.get('data').get('token')
            self.token = token
            return 1
        else:
            print(self.base_url)
            h = requests.get(url=self.base_url)
            return self.check_login(h, True, True)

    def check_login(
            self,
            h: object,
            flag: Optional[bool]=False,
            check_point: Optional[bool]=False
        ):
        """oneD12, check user login information.
        
        Args:
            h: 
                class:`Response <Response>` object.
            flag:
                do you need to output integral values. 
                A value of True requires querying points, 
                while a value of False does not require querying points.Defaults to False.
            check_point: 
                do you need to query user points. 
                If the value is True, the integral value is output,
                but if the value is False, the integral value does not need to be output.Defaults to False.

        Raises:
            Exception: Insufficient points.

        Returns:
            int: oneD12, check login status, 1 indicates authentication passed, 0 indicates failure
        """
        content = bs(h.text, "html.parser")
        token_element = content.find_all('p', id='loginMsg')
        user_point_element = content.find_all('p', id='integral')
        ret = 0
        for e in token_element:
            token = str(e).split(
                '登录返回的结果---&gt;')[1].split('</p>')[0]  # 登录失败，直接返回
            token = eval(token)
            if 'msg' in token:
                ret = token.get('msg')
                print(ret)
                return 0
            else:
                self.token = token.get('token')
                print(self.token)
                if not check_point:
                    return 1

        if check_point:
            for e in user_point_element:
                user_point = str(e).split('用户积分---&gt;')[1].split('</p>')[0]
                if '积分不足' in user_point:  # 积分标签中存在 积分不足 直接返回
                    print('积分不足!')
                    raise Exception('积分不足')
                    # return 0
                else:
                    if flag:
                        print(f'您已成功登入云平台，您账号里现在有{user_point}积分')
                    return 1

    def create_experiment(
            self,
            exp_name: str
        ):
        """create a new experiment, the new one is the experiment set ID.

        Args:
            exp_name: new experiment collection Name

        Returns:
            Union[int, str]: 0 failed, not 0 successful, success returns the experimental set id
        """
        if self.login_key:
            url = f'{self.base_url}/sdk/api/multiple/experiment/save'
            print('当前创建实验使用的机器名:', self.machine_name)
            data = {"experimentClipId": "", "name": exp_name,
                    "machineName": self.machine_name, "source": 'SDK'}
            headers = {"sdk_token": self.token}
            res = requests.post(url, json=data, headers=headers)
            status_code = res.status_code
            if status_code != 200:
                return 0
            result = json.loads(res.text)
            code = result.get('code', -1)
            msg = result.get('msg', '创建实验失败')
            if code != 0:
                print(f'创建实验失败：{msg}')
                return 0
            lab_id = result.get('data').get('lab_id')
            return lab_id
        else:
            sleep(random.randint(0, 15)*0.3+round(random.uniform(0, 1.5), 2))
            url = self.base_url + f'&expName={exp_name}'
            h = requests.get(url=url)
            content = bs(h.text, "html.parser")
            ret_check_login = self.check_login(h)
            if not ret_check_login:
                return ret_check_login

            create_experiment_element = content.find_all('p', id='addExp')
            for e in create_experiment_element:
                lab_id = str(e).split('新建实验返回的结果---&gt;')[1].split('</p>')[0]
                if 'msg' in lab_id:
                    exp_result = eval(lab_id)
                    if isinstance(exp_result, dict):
                        msg = exp_result.get('msg')
                        print(f'创建实验失败, {msg}')
                        return 0

                if not self.full_expr_record:
                    self.exp = {}

                self.exp[lab_id] = {}
                self.exp[lab_id]['lab_name'] = exp_name
                return lab_id
            print("创建实验失败, 没有返回结果")
            return 0

    def save_experiment(
            self,
            lab_id: str,
            exp_data: str,
            version: str
        ):
        """save the experiment and return the experiment ID.

        Args:
            lab_id: 
                the result returned by the create_experiment interface, experimental set id
            exp_data: 
                experimental content, qics
            version: 
                version description
        
        Examples:
            the input parameter can be the following value:

                lab_id: XXX
                exp_data:
                    X Q1
                    Y Q12
                    S Q3
                    SD Q15
                    T Q12
                    TD Q3
                    Z Q12
                    H Q1
                    RX Q3 2.78
                    RY Q9 1.97
                    RXY Q15 1.23 3.04
                    X2P Q1
                    X2M Q1
                    Y2P Q3
                    Y2M Q12
                    X Q19
                    CZ Q1 Q7
                    RZ Q8 2.16
                    I Q1 100
                    B Q1 Q12 Q3
                    M Q15 Q12 Q5 Q6

        Returns:
            Union[int, str]: 0 failed, not 0 successful, success returns the experiment id
        """
        exp_data = exp_data.upper()
        exp_data = self.get_experiment_data(exp_data)
        if self.login_key:
            url = self.base_url + '/sdk/api/multiple/experiment/detail/save'
            data = {
                "circuit": exp_data, "lab_id": lab_id,
                "language": "qcis", "version": version,
                "machineName": self.machine_name
            }
            headers = {"sdk_token": self.token}
            res = requests.post(url, json=data, headers=headers)
            status_code = res.status_code
            if status_code != 200:
                return 0
            result = json.loads(res.text)
            code = result.get('code', -1)
            msg = result.get('msg', '保存实验失败')
            if code != 0:
                print(f'保存实验失败：{msg}')
                return 0
            save_result = result.get('data').get('exp_id')
        else:
            sleep(random.randint(0, 15)*0.3+round(random.uniform(0, 1.5), 2))
            url = self.base_url + f'&expId={lab_id}&expData={exp_data}'
            h = requests.get(url=url)
            content = bs(h.text, "html.parser")
            ret_check_login = self.check_login(h)
            if not ret_check_login:
                return ret_check_login

            save_result_element = content.find_all('p', id='saveExp')
            for e in save_result_element:
                save_result = str(e).split(
                    '保存实验返回的结果---&gt;')[1].split('\n  </p>')[0]
                try:
                    save_exp = eval(save_result)
                    if 'code' in save_exp:
                        print(f"保存实验失败, {save_exp.get('msg')}")
                        return 0
                    else:
                        print('保存实验失败, 返回信息中不存在code')
                        return 0
                except:
                    if len(save_result.split(',')) > 1:
                        print(f"保存实验失败, {save_result.split(',')[1]}")
                        return 0
                    else:
                        if u'\u4e00' <= save_result <= u'\u9fff':
                            print(f'保存实验失败, {save_result}')
                            return 0

            if lab_id in self.exp:
                # 追加并且exp_detail存在于字典中
                if self.full_expr_record and 'exp_detail' in self.exp[lab_id]:
                    self.exp[lab_id]['exp_detail'][save_result] = {
                        'version_name': save_result, 'run_detail': []}
                else:  # 覆盖，不管是full_expr_record为True还是exp_detail不存在于字典中，都需要重新定义exp_detail
                    exp_detail = {}
                    exp_detail[save_result] = {
                        'version_name': save_result, 'run_detail': []}
                    self.exp[lab_id]['exp_detail'] = exp_detail
            else:
                print('保存实验版本编号无法保存, 信息中不存在当前实验集id')

        return save_result

    def run_experiment(
            self,
            exp_id: str,
            num_shots: Optional[int]=12000
        ):
        """running the experiment returns the query result id.

        Args:
            exp_id: 
                the result returned by the save_experiment interface, experimental id
            num_shots: 
                number of repetitions per experiment. Defaults to 12000.

        Returns:
            Union[int, str]: 0 failed, not 0 successful, success returns the query id
        """
        if self.login_key:
            url = self.base_url + '/sdk/api/multiple/experiment/temporary/save'
            data = {"circuit": "", "exp_id": exp_id,
                    "lab_id": "", "query_id": "",
                    "shots": num_shots, "version": "",
                    "machineName": self.machine_name, "source": 'SDK'}
            headers = {"sdk_token": self.token}
            res = requests.post(url, json=data, headers=headers)
            status_code = res.status_code
            if status_code != 200:
                return 0
            result = json.loads(res.text)
            code = result.get('code', -1)
            msg = result.get('msg', '运行实验失败')
            if code != 0:
                print(f'运行实验失败：{msg}')
                return 0
            run_result = result.get('data').get('query_id')
            return run_result
        else:
            sleep(random.randint(0, 15)*0.3+round(random.uniform(0, 1.5), 2))
            url = self.base_url + f'&expDetailId={exp_id}&shots={num_shots}'
            h = requests.get(url=url)
            content = bs(h.text, "html.parser")
            ret_check_login = self.check_login(h, check_point=True)
            if not ret_check_login:
                return ret_check_login

            run_result_element = content.find_all('p', id='runExp')
            for e in run_result_element:
                run_result = str(e).split(
                    '运行实验返回的结果---&gt;')[1].split('</p>')[0]

            try:
                if not self.machine_name:
                    run_result = int(run_result)

                # 根据exp_id查询初lab_id
                lab_id = None
                for lab in self.exp:
                    exp_detail_dir = self.exp[lab].get('exp_detail', None)
                    if exp_detail_dir:
                        if exp_id in exp_detail_dir:
                            lab_id = lab

                if lab_id:
                    if self.full_expr_record:  # 追加
                        self.exp[lab_id]['exp_detail'][exp_id]['run_detail'].\
                            append(run_result)
                    else:
                        self.exp[lab_id]['exp_detail'][exp_id]['run_detail'] = [
                            run_result]
                else:
                    print('提交实验后的查询编号无法保存，信息中不存在当前实验集id活实验版本id')

                return run_result
            except:
                print(f'运行实验失败, {run_result}')
                return 0

    def query_experiment(
            self,
            query_id: str,
            max_wait_time: Optional[int]=60,
            result_type=2
        ):
        """query experimental results

        Args:
            query_id: 
                the result returned by the run_experiment interface, experimental set id
            max_wait_time: 
                maximum waiting time for querying experiments. Defaults to 60.
            result_type: 
                election of return value type of other quantum computer except oneD12,
                result_type value of 0 represents the raw data, and a value of 1 represents the probability valueDefaults to 2.

        Raises:
            Exception: query experiment result type error

        Returns:
            Union[int, str]: 0 failed, not 0 successful, success returns the experimental result
        """
        if self.login_key is None:
            sleep(random.randint(0, 15)*0.3+round(random.uniform(0, 1.5), 2))
        t0 = time()
        while time()-t0 < max_wait_time:
            try:
                if self.login_key:
                    if result_type not in [0, 1, 2]:
                        raise Exception('查询实验结果类型错误')
                    url = self.base_url + '/sdk/api/multiple/experiment/find/results'
                    data = {"circuit": "", "exp_id": "", "lab_id": "",
                            "quantumComputer": "", "query_id": query_id,
                            "shots": 0, "version": "string", "type": result_type}
                    headers = {"sdk_token": self.token}
                    res = requests.post(url, json=data, headers=headers)
                    status_code = res.status_code
                    if status_code != 200:
                        return 0
                    result = json.loads(res.text)
                    code = result.get('code', -1)
                    msg = result.get('msg', '查询实验失败')
                    if code != 0:
                        print(f'查询实验失败：{msg}')
                        return 0
                    query_exp = result.get('data', None)
                    if query_exp:
                        return query_exp
                else:
                    url = self.base_url + f'&download={query_id}'
                    h = requests.get(url=url)
                    content = bs(h.text, "html.parser")
                    ret_check_login = self.check_login(h)
                    if not ret_check_login:
                        return ret_check_login

                    query_result_element = content.find_all(
                        'p', id='downloadExp')
                    for e in query_result_element:
                        query_result = str(e).split(
                            '下载实验返回的结果---&gt;')[1].split('  </p>')[0]
                        query_exp = eval(query_result)
                        if 'code' in query_exp:
                            msg = query_exp.get('msg')
                        else:
                            return query_exp
            except:
                import traceback
                print(traceback.format_exc())
                sleep_time = random.randint(
                    0, 15)*0.3+round(random.uniform(0, 1.5), 2)
                print(f'查询实验结果请等待: {{:.2f}}秒'.format(sleep_time))
                sleep(sleep_time)
                continue
        print(f'查询实验结果失败')
        return 0

    def submit_job(
            self,
            circuit: Optional[str]=None,
            exp_name: Optional[str]="exp0",
            parameters: Optional[List]=None,
            values: Optional[List]=None,
            num_shots: Optional[int]=12000,
            lab_id: Optional[str]=None,
            exp_id: Optional[str]=None,
            version: Optional[str]="version01"
        ):
        """submit experimental tasks

        Args:
            circuit: 
                experimental content, qics. Defaults to None.
            exp_name:
                new experiment collection Name. Defaults to 'exp0'.
            parameters: 
                parameters that need to be assigned in the experimental content. Defaults to None.
            values: 
                The values corresponding to the parameters that need to be assigned in the experimental content. Defaults to None.
            num_shots:
                number of repetitions per experiment. Defaults to 12000.
            lab_id: 
                the result returned by the create_experiment interface, experimental set id. Defaults to None.
            exp_id: 
                the result returned by the save_experiment interface, experimental id. Defaults to None.
            version: 
                version description. Defaults to 'version01'.

        Returns:
            Union[int, str]: 0 failed, not 0 successful, success returns the query id.
        """
        if circuit:
            circuit = self.assign_parameters(
                circuit.upper(), parameters, values)
            if not circuit:
                print('无法为线路赋值，请检查线路，参数和参数值之后重试')
                return 0
        if self.login_key:
            url = self.base_url + '/sdk/api/multiple/experiment/temporary/save'
            data = {"circuit": circuit, "exp_id": exp_id,
                    "lab_id": lab_id, "name": exp_name,
                    "shots": num_shots, "version": version,
                    "machineName": self.machine_name, "source": 'SDK'}
            headers = {"sdk_token": self.token}
            res = requests.post(url, json=data, headers=headers)
            status_code = res.status_code
            if status_code != 200:
                return 0
            result = json.loads(res.text)
            code = result.get('code', -1)
            msg = result.get('msg', '运行实验失败')
            if code != 0:
                print(f'运行实验失败：{msg}')
                return 0
            run_result = result.get('data').get('query_id')
            return run_result
        else:
            try:
                flag = True
                if circuit and exp_id:
                    # circuit 与 exp_id 冲突，不执行
                    print('线路和实验版本冲突，无法执行')
                    return 0
                elif circuit and lab_id:
                    # 查看lab_id在字典中是否存在
                    if lab_id not in self.exp:
                        print(f'{lab_id}不存在当前字典中')
                        return 0
                    # 如存在save--run
                elif circuit:
                    # 按照lab_name，# create--save--run
                    lab_id = self.create_experiment(exp_name)
                    if not lab_id:
                        return 0
                elif exp_id and lab_id:
                    flag = False
                    # 检查字典lab_id和exp_id是否匹配
                    # 匹配成功 run
                    if lab_id not in self.exp or exp_id not in self.exp.get(lab_id, {}).get('exp_detail', {}):
                        print(f'输入的实验版本{exp_id}不属于该实验集{lab_id}下')
                        return 0
                elif exp_id:
                    # 查看字典中，是否存在exp_id
                    # 存在 run
                    for item in self.exp:
                        if exp_id in self.exp.get(item, {}).get('exp_detail', {}):
                            flag = False
                    if flag:
                        print('找不到实验版本对应的实验集')
                        return 0
                else:
                    print('没有待创建或已创建的实验可以执行')
                    return 0

                if flag:
                    exp_id = self.save_experiment(lab_id, circuit, version)
                    if not exp_id:
                        return 0
                # 提交实验
                query_id = self.run_experiment(exp_id, num_shots)
                if query_id:
                    return query_id
                else:
                    return 0

            except:
                print(traceback.format_exc())
                print('提交实验失败, 请检查参数信息')

            return 0

    def assign_parameters(
            self, 
            circuit: str, 
            parameters: List, 
            values: List
        ):
        """Check if the number of parameters, values match the circuit definition

        Args:
            circuit: 
                string, QCIS circuit definition with or without parameter place holder
            parameters: 
                list or ndarray of strings, parameters to be filled
            values: 
                list or ndarray of floats, values to be assigned

        Returns:
            circuit: circuit with parameters replaced by values or empty string
            empty string occurs when errors prevents parameters to be assigned
        """
        circuit = circuit.upper()
        p = re.compile(r'\{(\w+)\}')
        circuit_parameters = p.findall(circuit)
        if circuit_parameters:

            # 如果values为整数或浮点数，改为列表格式##########################################################
            if isinstance(values, (float, int)):
                values = [values]
            # 如果parameters为字符格式，改为列表格式#########################################################
            if isinstance(parameters, str):
                parameters = [parameters]
            # 将所有parameter变为大写， 否则set(parameters) != set(circuit_parameters) 不通过 ###############
            parameters = [p.upper() for p in parameters]

            if not values:
                error_message = f'线路含有参数{circuit_parameters}, 请提供相应的参数值'
                print(error_message)
                return ''

            else:
                if len(circuit_parameters) != len(values):
                    error_message = f'线路含有{len(circuit_parameters)}个参数, 您提供了{len(values)}个参数值'
                    print(error_message)
                    return ''

                elif parameters and len(circuit_parameters) != len(parameters):
                    error_message = f'线路含有{len(circuit_parameters)}个参数, 您提供了{len(parameters)}个参数'
                    print(error_message)
                    return ''

                elif set(parameters) != set(circuit_parameters):
                    error_message = '线路中的参数与您输入的参数名称不符'
                    print(error_message)
                else:
                    param_dic = {}
                    ############################# 这个转化可以删了 #########################################
                    # parameters_upper = [p.upper() for p in parameters]
                    for p, v in zip(parameters, values):
                        param_dic[p] = v
                    expData = circuit.format(**param_dic)
                    return expData

        elif parameters or values:
            error_message = '线路定义中不含有参数，无法接受您输入的参数或参数值'
            print(error_message)
            return ''
        else:
            expData = circuit
            return expData

    def get_experiment_data(self, circuit):
        """Parse circuit description and generate 
           experiment script and extract number of measured qubits.

        Args:
            circuit: 
                string, QCIS circuit

        Returns:
            expData: 
                string, transformed circuit
        """
        # get gates from circuit
        if self.login_key:
            gates_list = circuit.split('\n')
            gates_list_strip = [g.strip() for g in gates_list if g]
            gates_list_strip = [g for g in gates_list_strip if g]

            # transform circuit from QCIS to expData
            expData = '\n'.join(gates_list_strip)
            return expData
        else:
            gates_list = circuit.split('\n')
            gates_list_strip = [g.strip() for g in gates_list if g]
            gates_list_strip = [g for g in gates_list_strip if g]

            # transform circuit from QCIS to expData
            expData = ';'.join(gates_list_strip)
            return expData

    def load_exp_data(
            self,
            filepath: Optional[str]='lab_info.json'):
        """query the submitted experimental information for the oneD12 quantum compute.

        Args:
            filepath: 
                file path. Defaults to 'lab_info.json'.

        Returns:
            Dict: submitted experimental information.
            None: the file does not exist or the file content is empty.
        """
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            with open(filepath, 'r') as f:
                exp = json.load(f)
            return exp
        print('文件不存在或者文件内容为空')

    def save_exp_data(
            self,
            filename: Optional[str]='lab_info.json', 
            mode: Optional[str]='w'):
        """save the submitted experiment content for oneD12 quantum computer.

        Args:
            filename: file name. Defaults to 'lab_info.json'.
            mode: file operation mode, 'w' or 'r'. Defaults to 'w'.
        """
        if self.exp:
            with open(filename, mode) as f:
                json.dump(self.exp, f)

    def set_machine(
            self, 
            machine_name: str
        ):
        """except oneD12 quantum computer, set the machine name.

        Args:
            machine_name: name of quantum computer.

        Raises:
            Exception: Failed to set machine name, request interface failed.
            Exception: Failed to set machine name.
        """
        url = f'{self.base_url}/sdk/api/multiple/experiment/find/quantum/computer'
        data = {
            "experimentClipId": "",
            "machineName": machine_name,
            "name": "",
            "source": "SDK"
        }
        headers = {"sdk_token": self.token}
        res = requests.post(url, json=data, headers=headers)
        status_code = res.status_code
        if status_code != 200:
            raise Exception('设置机器名失败，请求接口失败')
        result = json.loads(res.text)
        code = result.get('code', -1)
        msg = result.get('msg', '设置机器名失败')
        if code != 0:
            print(f'设置机器名失败：{msg}')
            raise Exception(f'设置机器名失败，{msg}')
        self.machine_name = machine_name

    def download_config(
            self, 
            down_file: Optional[bool]=True
        ):
        """except oneD12 quantum computer, download experimental parameters.

        Args:
            down_file: 
                the parameter is True to write to the file, and False to directly return the experimental parameters. Defaults to True.

        Returns:
           Union[int, str]: 0 failed, not 0 successful, success returns the experimental parameters.
        """
        url = f'{self.base_url}/sdk/api/multiple/experiment/config/download'
        data = {
            "name": self.machine_name
        }
        headers = {"sdk_token": self.token}
        res = requests.post(url, json=data, headers=headers)
        status_code = res.status_code
        if status_code != 200:
            return 0
        result = json.loads(res.text)
        if 'code' in result:
            msg = result.get('msg', '下载实验参数失败')
            print(f'下载实验参数失败:{msg}')
            return 0
        cur_time = self.current_time()
        if down_file:
            with open(f'./{self.machine_name}_config_param_{cur_time}.json', 'w') as f:
                f.write(json.dumps(result))
        return result

    def convert_qasm_to_qcis(
            self,
            qasm: str, 
            qubit_map: Optional[Dict]=None
        ):
        """convert qasm to qcis.

        Args:
            qasm: 
                qasm.
            qubit_map: 
                Number mapping in qasm, where the value is None, 
                directly maps bits based on the format of number plus 1. Defaults to None.
        Raises:
            Exception: language conversion failed.

        Returns:
            str: simplified qcis.
        """
        qcis_raw = self.qasmtoqcis.convert_qasm_to_qcis(
            qasm, qubit_map=qubit_map)
        simplity_qcis = self.qasmtoqcis.simplify(qcis_raw)
        return simplity_qcis

    def convert_qasm_to_qcis_from_file(
            self, 
            qasm_file: str, 
            qubit_map: Optional[Dict]=None):
        """Read qasm from file and convert it to qcis

        Args:
            qasm_file: 
                qasm file.
            qubit_map: 
                Number mapping in qasm, where the value is None, 
                directly maps bits based on the format of number plus 1. Defaults to None.

        Raises:
            Exception: language conversion failed.

        Returns:
            str: simplified qcis.
        """
        qcis_raw = self.qasmtoqcis.convert_qasm_to_qcis_from_file(
            qasm_file, qubit_map=qubit_map)
        simplity_qcis = self.qasmtoqcis.simplify(qcis_raw)
        return simplity_qcis

    def convert_qcis_to_qasm(
            self, 
            qcis: str
        ):
        """convert qcis to qasm.

        Args:
            qcis: qcis

        Returns:
            str: converted qasm.
        """
        qasm_circuit = self.qcistoqasm.convert_qcis_to_qasm(qcis)
        return qasm_circuit

    def qcis_check_regular(
            self, 
            qcis_raw: str):
        """qcis regular check,normal returns 1, abnormal returns 0

        Args:
            qcis_raw: qcis

        Returns:
            Union[int, str]: 0 failed, not 0 successful, successfully returned the input qics.
        """
        if self.login_key:
            quantum_computer_name = self.machine_name
            url = f'{self.base_url}/server/api/multiple/experiment/verify'
        else:
            quantum_computer_name = "oneD12"
            url = f'{self.cloud_url}/server/api/multiple/experiment/verify'
        data = {
            "quantumComputerName": quantum_computer_name,
            "qcis": qcis_raw
        }
        headers = {"sdk_token": self.token}
        res = requests.post(url, json=data, headers=headers)
        status_code = res.status_code
        if status_code != 200:
            return 0
        result = json.loads(res.text)
        code = result.get('code', -1)
        msg = result.get('msg', 'qcis检验失败')
        if code != 0:
            print(f'qcis检验失败: {msg}')
            return 0
        return qcis_raw

    def simplify(
            self, 
            qcis_raw: str):
        """simplification of qcis lines.

        Args:
            qcis_raw: qcis

        Returns:
            str: simplified qcis.
        """
        new_qcis_raw = self.qcis_check_regular(qcis_raw)
        simplity_qcis = self.qasmtoqcis.simplify(new_qcis_raw)
        return simplity_qcis

    def current_time(self):
        """get the current time

        Returns:
            str: time string
        """
        timestamp = datetime.datetime.fromtimestamp(time())
        str_time = timestamp.strftime('%Y%m%d%H%M%S')
        return str_time

    def readout_data_to_state_probabilities(
            self, 
            result
        ):
        state01 = result.get('results')
        basis_list = []
        basis_content = ''.join(
            [''.join([str(s) for s in state]) for state in state01[1:]])
        qubits_num = len(state01[0])  # 测量比特个数
        for idx in range(qubits_num):
            basis_result = basis_content[idx: len(basis_content): qubits_num]
            basis_list.append(
                [True if res == "1" else False for res in basis_result])
        return basis_list

    # 读取数据转换成量子态概率全部返回
    def readout_data_to_state_probabilities_whole(
            self, 
            result: Dict):
        """read data and convert it into a quantum state probability, all returns.

        Args:
            result: the results returned after query_experiment.

        Returns:
            Dict: probability
        """
        basis_list = self.readout_data_to_state_probabilities(result)
        probabilities = self.original_onversion_whole(basis_list)
        return probabilities

    # 读取数据转换成量子态概率部分，概率为0不返回
    def readout_data_to_state_probabilities_part(
            self, 
            result: Dict):
        """read data and convert it into a quantum state probability, do not return with a probability of 0.

        Args:
            result: the results returned after query_experiment.

        Returns:
            Dict: probability
        """
        basis_list = self.readout_data_to_state_probabilities(result)
        probabilities = self.original_onversion_part(basis_list)
        return probabilities

    def original_onversion_whole(
            self, 
            state01):
        # 当state01为一维时转换成二维数据
        if isinstance(state01[0], bool):
            state01 = [state01]
        n = len(state01)  # 读取比特数
        # 测量比特概率限制
        # if n > MAX_QUBIT_NUM:
        #     print(f'Number of qubits > {MAX_QUBIT_NUM}, cannot calculate probabilities.')
        counts = [0] * (2 ** n)
        state01_T = np.transpose(state01)  # 转置
        numShots = len(state01_T)  # 测量重复次数
        # 统计所有numShots 列
        for num in range(numShots):
            k = 0
            for i in range(n):
                k += state01_T[num][i] * (2 ** i)
            counts[k] += 1
        # 计算概率
        # P=[counts[k]/numShots for k in range(2**n)]
        P = {bin(k)[2:].zfill(n): counts[k]/numShots for k in range(2**n)}
        return P

    def original_onversion_part(
            self, 
            state01):
        # 当state01为一维时转换成二维数据
        if isinstance(state01[0], bool):
            state01 = [state01]
        n = len(state01)  # 读取比特数
        # 测量比特概率限制
        # if n > MAX_QUBIT_NUM:
        #     raise Exception(f'Number of qubits > {MAX_QUBIT_NUM}, cannot calculate probabilities.')
        counts = {}
        state01_T = np.transpose(state01)  # 转置
        numShots = len(state01_T)  # 测量重复次数
        # 统计所有numShots 列
        for num in range(numShots):
            k = 0
            for i in range(n):
                k += state01_T[num][i] * (2 ** i)
            prob_state = bin(k)[2:].zfill(n)
            if prob_state not in counts:
                counts[prob_state] = 1
            else:
                counts[prob_state] += 1
        # 计算概率
        # P=[counts[k]/numShots for k in range(2**n)]
        P = {k: v/numShots for k, v in counts.items()}
        return P

    # 量子态概率矫正
    def probability_calibration(
            self, 
            result: Dict, 
            config_json: Optional[Dict]=None):
        """correction of the measured probability of 01 quantum state.

        Args:
            result:
                the results returned after query_experiment.
            config_json: 
                experimental parameters of quantum computer. 
                config_json value is None, read the latest experimental parameters for calculation.
                Defaults to None.

        Raises:
            Exception: cannot calibrate probability with fidelity.

        Returns:
            Dict: corrected probability.
        """
        CM_CACHE = {}
        if config_json is None:
            config_json = self.download_config(down_file=False)
        qubit_num = [f'Q{i}' for i in result.get('results')[0]]
        n = len(qubit_num)  # 测量比特个数
        qubits = config_json['readout']['readoutArray']['|0> readout fidelity']['qubit_used']
        readout_fidelity0 = config_json['readout']['readoutArray']['|0> readout fidelity']['param_list']
        readout_fidelity1 = config_json['readout']['readoutArray']['|1> readout fidelity']['param_list']
        iq2probFidelity = [[readout_fidelity0[qubits.index(
            q)], readout_fidelity1[qubits.index(q)]] for q in qubit_num]
        P = self.readout_data_to_state_probabilities_whole(result)
        Pm = list(P.values())
        if not isinstance(iq2probFidelity[0], list):
            iq2probFidelity = [iq2probFidelity]
        f = tuple([float(fi) for fi in sum(iq2probFidelity, [])])
        if f not in CM_CACHE:
            inv_CM = 1
            for k in iq2probFidelity[::-1]:
                F00 = k[0]
                F11 = k[1]
                if F00 + F11 == 1:
                    raise Exception(
                        f'Cannot calibrate probability with fidelity: [{F00}, {F11}]')
                inv_cm = np.array(
                    [[F11, F11 - 1], [F00 - 1, F00]]) / (F00 + F11 - 1)
                inv_CM = np.kron(inv_CM, inv_cm)
            CM_CACHE[f] = inv_CM
        else:
            inv_CM = CM_CACHE[f]
        Pi = np.dot(inv_CM, (np.array(Pm, ndmin=2).T))
        Pi = {bin(idx)[2:].zfill(n): k[0] for idx, k in enumerate(Pi)}
        return Pi

    def qcis_mapping_isq(
            self,
            qcis_circuit: str,
            initial_layout: Optional[Dict]=None,
            objective: Optional[str]='size',
            seed: Optional[int]=None,
            use_post_opt: Optional[bool]=False):
        """The script transpiles qcis string by searching for a mapping from virtual to physical qubit 
           and a swap strategy such that the circuit described by qcis can be fitted into a hardware 
           described by the coupling_map, in the meanwhile reduces circuit depth.

        Args:
            qcis_circuit: _description_
            initial_layout: 
                Initial position of virtual qubits on physical qubits.
                If given, this is the initial state in search of virtual to physical qubit mapping
                e.g.:
                    {0:4, 1:1, 2:5, 3:2, 4:0, 5:3}. Defaults to None.
            objective: 
                size: min. # of added swaps
                depth: min. depth
                no_swap: try best to find an initial mapping requiring no swaps; raise 
                an error if fail. Defaults to 'size'.
            seed: 
                Set random seed for the stochastic part of the tranpiler. Defaults to None.
            use_post_opt: 
                we provide a genetic alg. which utilizes exchange rules for
                swaps to futher min. depth. Defaults to False.

        raised:
            TranspileError:
                if graph specified by coupling map is disconnected.

        Returns:
            str: qcis string after transpilation
        """
        config_json = self.download_config(down_file=False)
        try:
            qasm_circuit = self.convert_qcis_to_qasm(qcis_circuit)
            cur_time = self.current_time()
            qpu_file = f'./{self.machine_name}_config_param_{cur_time}.json'
            with open(qpu_file, 'w') as f:
                f.write(json.dumps(config_json))
            qasm_transpiled, _, _, _ = transpile(qasm_circuit,
                                                 qpu_file,
                                                 initial_layout=initial_layout,
                                                 objective=objective,
                                                 seed=seed,
                                                 use_post_opt=use_post_opt)
            simplity_qcis = self.convert_qasm_to_qcis(qasm_transpiled)
            return simplity_qcis
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print('circuit mapping error, will submit using the original route')
            return qcis_circuit

    def qcis_mapping_sabre(
            self, 
            qcis_circuit: str):
        '''The script transpiles qcis string by searching for a mapping from virtual to physical qubit 
           and a swap strategy such that the circuit described by qcis can be fitted into a hardware 
           described by the coupling_map, in the meanwhile reduces circuit depth.

        Args:
            qcis_circuit: qcis circuit

        Returns:
            str : qcis after mapping
        '''
        config_json = self.download_config(down_file=False)
        try:
            # qcis转换成qasm并写入qasm_file中
            qasm_circuit = self.qcistoqasm.convert_qcis_to_qasm(qcis_circuit)
            qasm_file = 'temp/qasm.qasm'
            with open(qasm_file, 'w') as f:
                f.write(qasm_circuit)
            sabre = SabreMapper()
            # 组装chip_info_fn映射信息
            chip_info_fn = {}
            couplings = []
            coupler_maps = config_json.get('overview').get('coupler_map')
            coupler_used = config_json.get('twoQubitGate').get(
                'czGate').get('gate error').get('qubit_used')
            cz_gate_error = config_json.get('twoQubitGate').get(
                'czGate').get('gate error').get('param_list')
            for coupler, error in zip(coupler_used, cz_gate_error):
                fidelity = 1 - error
                coupler_qubit_map = coupler_maps.get(coupler)
                couplings.append(
                    {"fidelity": fidelity, "qubit pair": coupler_qubit_map})
            chip_info_fn['couplings'] = couplings
            qubit_used = config_json.get('qubit').get(
                'singleQubit').get('gate error').get('qubit_used')
            qubit_gate_error = config_json.get('qubit').get(
                'singleQubit').get('gate error').get('param_list')
            qubit_fidelity = {}
            for qubit, error in zip(qubit_used, qubit_gate_error):
                qubit_fidelity[qubit] = 1 - error
            chip_info_fn['fidelity'] = qubit_fidelity
            chip_info_fn['has multiple chips'] = False
            chip_info_fn['qubits'] = qubit_used

            chip_info_fn_file = "temp/chip_info_fn.json"
            mapped_qasm_fn_file = "temp/mapped_qasm_fn.qasm"
            qubit_mapping_fn_file = "temp/qubit_mapping_fn.json"
            with open(chip_info_fn_file, 'w') as f:
                json.dump(chip_info_fn, f)
            # 调用quMapper做mapping操作
            success = sabre.map_schedule(
                qasm_file, chip_info_fn_file, mapped_qasm_fn_file, qubit_mapping_fn_file)
            if success:
                with open(qubit_mapping_fn_file, 'r') as f:
                    qubit_mapping_fn = json.load(f)
                qubit_map = qubit_mapping_fn.get('physical qubits idx')
                # mapping成功，将转换后的qasm转为qcis，其中编号根据physical qubits idx做映射
                simplity_qcis = self.convert_qasm_to_qcis_from_file(
                    mapped_qasm_fn_file, qubit_map)
                return simplity_qcis
        except Exception as e:
            print(e)
            print('circuit mapping error, will submit using the original route')
            return qcis_circuit
    
    def get_experiment_circuit(
            self,
            exp_id: str):
        if self.login_key:
            url = f'{self.base_url}/sdk/api/multiple/experiment/detail/{exp_id}'
            headers = {"sdk_token": self.token}
            res = requests.get(url, headers=headers)
            status_code = res.status_code
            if status_code != 200:
                return 0
            result = json.loads(res.text)
            code = result.get('code', -1)
            msg = result.get('msg', '查询实验线路失败')
            if code != 0:
                print(f'查询实验线路: {msg}')
                return 0
            circuit = result.get('data')
            return circuit
