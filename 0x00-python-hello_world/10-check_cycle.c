#include "lists.h"
/**
 * check_cycle - function to detect cycles in lists
 *
 * @list: ponter to head
 * Return: 1 if cycle found, 0 if no cycles
 */
int check_cycle(listint_t *list)
{
	listint_t *adv, *advv;

	if (list == NULL || list->next == NULL)
		return (0);
	adv = list->next;
	advv = list->next->next;
	while (adv && advv && advv->next)
	{
		if (adv == advv)
		{
			return (1);
		}
		adv = adv->next;
		advv = advv->next->next;
	}
	return (0);
}
