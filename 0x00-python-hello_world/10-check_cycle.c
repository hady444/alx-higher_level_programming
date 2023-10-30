#include "lists.h"
/**
 * check_cycle - function to detect cycles in lists
 *
 * @list: ponter to head
 * Return: 1 if cycle found, 0 if no cycles
 */
int check_cycle(listint_t *list)
{
	listint_t *adv;

	if (list == NULL)
		return (0);
	adv = list;
	while (adv->next != NULL)
	{
		if (adv->next == list)
		{
			return (1);
		}
		adv = adv->next;
	}
	return (0);
}
