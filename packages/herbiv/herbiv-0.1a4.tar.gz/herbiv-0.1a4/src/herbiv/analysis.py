from . import get
from . import compute
from . import output


def from_tcm(tcm,
             score=900,
             re=True):
    r"""
    进行逆向网络药理学分析
    :param tcm: 列表类型，拟分析的中药的中文名称
    :param score: int类型，仅combined_score大于等于score的记录会被筛选出
    :param re: 布尔类型，是否返回原始分析结果
    :return: tcm: pd.DataFrame类型，中药信息
    :return: tcm_chem_links: pd.DataFrame类型，中药-成分信息
    :return: chem_protein_links: pd.DataFrame类型，化合物-蛋白质（靶点）信息
    """

    tcm = get.get_tcm('cn_name', tcm)
    tcm_chem_links = get.get_tcm_chem_links('HVMID', tcm['HVMID'])
    chem = get.get_chemicals('HVCID', tcm_chem_links['HVCID'])
    chem_protein_links = get.get_chem_protein_links('HVCID', chem['HVCID'], score)
    protein = get.get_proteins('Ensembl_ID', chem_protein_links['Ensembl_ID'])
    chem, tcm = compute.score(chem_protein_links, chem, tcm_chem_links, tcm)

    if re:
        return tcm, tcm_chem_links, chem, chem_protein_links, protein


def from_genes(genes,
               score=900,
               out_for_cytoscape=True,
               re=True,
               path='result/'):
    r"""
    进行逆向网络药理学分析
    :param genes: list类型，存储拟分析蛋白（基因）在STITCH中的ID
    :param score: int类型，仅combined_score大于等于score的记录会被筛选出
    :param out_for_cytoscape: 布尔类型，是否输出用于Cytoscape绘图的文件
    :param re: 布尔类型，是否返回原始分析结果
    :param path: 字符串类型，存放结果的目录
    :return: tcm: pd.DataFrame类型，中药信息
    :return: tcm_chem_links: pd.DataFrame类型，中药-成分信息
    """
    proteins = get.get_proteins('Ensembl_ID', genes)
    chem_protein_links = get.get_chem_protein_links('Ensembl_ID', proteins['Ensembl_ID'], score)
    chem = get.get_chemicals('HVCID', chem_protein_links['HVCID'])
    tcm_chem_links = get.get_tcm_chem_links('HVCID', chem['HVCID'])
    tcm = get.get_tcm('HVMID', tcm_chem_links['HVMID'])
    chem, tcm = compute.score(chem_protein_links, chem, tcm_chem_links, tcm)

    if out_for_cytoscape:
        output.out_for_cyto(chem_protein_links, chem, proteins, tcm_chem_links, tcm, path)

    if re:
        return tcm, tcm_chem_links, chem, chem_protein_links, proteins


def from_tcm_protein(tcm,
                     protein,
                     score=0,
                     out_for_cytoscape=True,
                     re=True,
                     path='result/'):
    r"""
    本函数用于对输入的中药和靶点“取交集“
    :param tcm: list类型，输入需要的中药的HVMID "HVMID"
    :param protein: list类型，输入所需靶点的序号 "Ensembl_ID"
    :return: chem: 返回两者共同的交集
    """

    tcm = get.get_tcm('cn_name', tcm)
    protein = get.get_proteins('Ensembl_ID', protein)
    tcm_chem_links = get.get_tcm_chem_links('HVMID', tcm['HVMID'])
    chem_protein_links = get.get_chem_protein_links('Ensembl_ID', protein['Ensembl_ID'], score)

    common = tcm_chem_links[tcm_chem_links['HVCID'].isin(chem_protein_links['HVCID'])]
    chem = chem_protein_links[chem_protein_links['HVCID'].isin(common['HVCID'])]
    chem = get.get_chemicals('HVCID', chem['HVCID'])
    chem.index = range(chem.shape[0])
    chem, tcm = compute.score(chem_protein_links, chem, tcm_chem_links, tcm)

    if out_for_cytoscape:
        output.out_for_cyto(chem_protein_links, chem, protein, tcm_chem_links, tcm, path)

    if re:
        return tcm, tcm_chem_links, chem, chem_protein_links, protein


if __name__ == '__main__':
    tcm, tcm_chem_links, chem, chem_protein_links, protein = from_tcm_protein(tcm=['柴胡', '黄芩'],
                                                                              protein=['ENSP00000381588',
                                                                                       'ENSP00000252519'],
                                                                              score=0,
                                                                              out_for_cytoscape=True,
                                                                              re=True)
    print(1)

    """tcm = get.get_tcm('cn_name', ['柴胡', '黄芩'])
    tcm_chem_links = get.get_tcm_chem_links('HVMID', tcm['HVMID'])
    chem_protein_links = get.get_chem_protein_links('Ensembl_ID', ['ENSP00000381588'])
    chem = pd.merge(chem_protein_links, tcm_chem_links, on='HVCID')"""
